from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def get_all_user_types(db: Session):
    try:
        user_types = db.query(models.UserTypeDB).all()
        return schemas.BaseResponseSchema(
            message="User types retrieved successfully",
            status_code=200,
            data=[
                schemas.UserTypeResponseSchema.from_orm(user_type)
                for user_type in user_types
            ])
    finally:
        db.close()


def get_user_type_by_id(user_type_id: int, db: Session):
    try:
        user_type = db.query(models.UserTypeDB).filter(
            models.UserTypeDB.id == user_type_id).first()
        if user_type is None:
            raise HTTPException(status_code=404, detail="User type not found")
        return schemas.BaseResponseSchema(
            message="User type retrieved successfully",
            status_code=200,
            data=schemas.UserTypeResponseSchema.from_orm(user_type))
    finally:
        db.close()


def create_user_type(user_type: schemas.UserTypeCreateSchema, db: Session):
    try:
        existing_user_type = db.query(models.UserTypeDB).filter(
            models.UserTypeDB.name == user_type.name).first()
        if existing_user_type:
            raise HTTPException(
                status_code=400,
                detail="Bu isimde bir kullanıcı tipi zaten mevcut")

        db_user_type = models.UserTypeDB(name=user_type.name)
        db.add(db_user_type)
        db.commit()
        db.refresh(db_user_type)
        return schemas.BaseResponseSchema(
            message="User type created successfully",
            status_code=201,
            data=schemas.UserTypeResponseSchema.from_orm(db_user_type))
    finally:
        db.close()


def update_user_type(user_type: schemas.UserTypeUpdateSchema, db: Session):
    try:
        db_user_type = db.query(models.UserTypeDB).filter(
            models.UserTypeDB.id == user_type.id).first()
        if db_user_type is None:
            raise HTTPException(status_code=404,
                                detail="Kullanıcı tipi bulunamadı")

        # Check if another user type with same name exists
        existing_user_type = db.query(models.UserTypeDB).filter(
            models.UserTypeDB.name == user_type.name, models.UserTypeDB.id
            != user_type.id).first()
        if existing_user_type:
            raise HTTPException(
                status_code=400,
                detail="Bu isimde başka bir kullanıcı tipi zaten mevcut")

        db_user_type.name = user_type.name
        db.commit()
        db.refresh(db_user_type)
        return schemas.BaseResponseSchema(
            message="User type updated successfully",
            status_code=200,
            data=schemas.UserTypeResponseSchema.from_orm(db_user_type))
    finally:
        db.close()


def delete_user_type(user_type: schemas.UserTypeDeleteSchema, db: Session):
    try:
        db_user_type = db.query(models.UserTypeDB).filter(
            models.UserTypeDB.id == user_type.id).first()
        if db_user_type is None:
            raise HTTPException(status_code=404, detail="User type not found")
        db.delete(db_user_type)
        db.commit()
        return schemas.BaseResponseSchema(
            message="User type deleted successfully",
            status_code=200,
            data=schemas.UserTypeResponseSchema.from_orm(db_user_type))
    finally:
        db.close()
