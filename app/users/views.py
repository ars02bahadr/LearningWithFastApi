from fastapi import HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from typing import List
import os
import uuid
from datetime import datetime
from sqlalchemy.orm import joinedload

# Şifreleme için context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fotoğraf yükleme ayarları
UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def save_picture(file: UploadFile, user_id: int) -> str:
    # Dosya uzantısını kontrol et
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Sadece jpg, jpeg ve png dosyaları yüklenebilir")

    # Uploads klasörünü oluştur
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # Benzersiz dosya adı oluştur
    unique_filename = f"{user_id}_{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Dosyayı kaydet
    try:
        contents = file.file.read()
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="Dosya boyutu 5MB'dan büyük olamaz")
        
        with open(file_path, "wb") as f:
            f.write(contents)
        return unique_filename
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dosya yüklenirken hata oluştu: {str(e)}")
    finally:
        file.file.close()

def get_all_users(db: Session):
    try:
        users = db.query(models.UserDB).all()
        return schemas.BaseResponseSchema(
            message="Users retrieved successfully",
            status_code=200,
            data=[schemas.UserResponseSchema.from_orm(user) for user in users]
        )
    finally:
        db.close()

def get_user_by_id(user_id: int, db: Session):
    try:
        user = db.query(models.UserDB)\
        .options(
            joinedload(models.UserDB.user_type),
            joinedload(models.UserDB.roles)
        ).filter(models.UserDB.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return schemas.BaseResponseSchema(
            message="User retrieved successfully",
            status_code=200,
            data=schemas.UserResponseSchema.from_orm(user)
        )
    finally:
        db.close()

def create_user(user: schemas.UserCreateSchema, db: Session):
    try:
        # Email kontrolü
        if db.query(models.UserDB).filter(models.UserDB.email == user.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")

        # Şifreyi hashle
        hashed_password = get_password_hash(user.password)

        # Kullanıcıyı oluştur
        db_user = models.UserDB(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=hashed_password,
            birth_date=user.birth_date,
            is_active=user.is_active,
            user_type_id=user.user_type_id
        )

        # Rolleri ekle
        if user.role_ids:
            roles = db.query(models.UserRoleDB).filter(models.UserRoleDB.id.in_(user.role_ids)).all()
            db_user.roles = roles

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # Fotoğraf yükle
        if user.picture:
            picture_filename = save_picture(user.picture, db_user.id)
            db_user.picture = picture_filename
            db.commit()
            db.refresh(db_user)

        return schemas.BaseResponseSchema(
            message="User created successfully",
            status_code=201,
            data=schemas.UserResponseSchema.from_orm(db_user)
        )
    finally:
        db.close()

def update_user(user: schemas.UserUpdateSchema, db: Session):
    try:
        db_user = db.query(models.UserDB).filter(models.UserDB.id == user.id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")

        # Email değişiyorsa kontrol et
        if user.email != db_user.email:
            if db.query(models.UserDB).filter(models.UserDB.email == user.email).first():
                raise HTTPException(status_code=400, detail="Email already registered")

        # Şifre değişiyorsa hashle
        if user.password:
            user.password = get_password_hash(user.password)
        else:
            user.password = db_user.password

        # Kullanıcı bilgilerini güncelle
        for key, value in user.dict(exclude_unset=True).items():
            if key == "role_ids":
                if value:
                    roles = db.query(models.UserRoleDB).filter(models.UserRoleDB.id.in_(value)).all()
                    db_user.roles = roles
            elif key == "picture":
                if value:
                    # Eski fotoğrafı sil
                    if db_user.picture:
                        old_file_path = os.path.join(UPLOAD_DIR, db_user.picture)
                        if os.path.exists(old_file_path):
                            os.remove(old_file_path)
                    # Yeni fotoğrafı yükle
                    picture_filename = save_picture(value, db_user.id)
                    db_user.picture = picture_filename
            else:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return schemas.BaseResponseSchema(
            message="User updated successfully",
            status_code=200,
            data=schemas.UserResponseSchema.from_orm(db_user)
        )
    finally:
        db.close()

def delete_user(user: schemas.UserDeleteSchema, db: Session):
    try:    
        db_user = db.query(models.UserDB).filter(models.UserDB.id == user.id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Fotoğrafı sil
        if db_user.picture:
            file_path = os.path.join(UPLOAD_DIR, db_user.picture)
            if os.path.exists(file_path):
                os.remove(file_path)
        
        db.delete(db_user)
        db.commit()
        return schemas.BaseResponseSchema(
            message="User deleted successfully",
            status_code=200,
            data=schemas.UserResponseSchema.from_orm(db_user)
        )
    finally:
        db.close()

