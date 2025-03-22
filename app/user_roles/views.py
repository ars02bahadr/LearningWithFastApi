from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def get_all_user_roles(db: Session):
    try:
        user_roles = db.query(models.UserRoleDB).all()
        return schemas.BaseResponseSchema(
            message="User roles retrieved successfully",
            status_code=200,
            data=[schemas.UserRoleResponseSchema.from_orm(user_role) for user_role in user_roles]
        )
    finally:
        db.close()

def get_user_role_by_id(user_role_id: int, db: Session):
    try:
        user_role = db.query(models.UserRoleDB).filter(models.UserRoleDB.id == user_role_id).first()
        if user_role is None:
            raise HTTPException(status_code=404, detail="User role not found")
        return schemas.BaseResponseSchema(
            message="User role retrieved successfully",
            status_code=200,
            data=schemas.UserRoleResponseSchema.from_orm(user_role)
        )
    finally:
        db.close()

def create_user_role(user_role: schemas.UserRoleCreateSchema, db: Session):
    try:
        db_user_role = models.UserRoleDB(name=user_role.name)
        db.add(db_user_role)
        db.commit()
        db.refresh(db_user_role)
        return schemas.BaseResponseSchema(
            message="User role created successfully",
            status_code=201,
            data=schemas.UserRoleResponseSchema.from_orm(db_user_role)
        )
    finally:
        db.close()

def update_user_role(user_role: schemas.UserRoleUpdateSchema, db: Session):
    try:
        db_user_role = db.query(models.UserRoleDB).filter(models.UserRoleDB.id == user_role.id).first()
        if db_user_role is None:
            raise HTTPException(status_code=404, detail="User role not found")
        db_user_role.name = user_role.name
        db.commit()
        db.refresh(db_user_role)
        return schemas.BaseResponseSchema(
            message="User role updated successfully",
            status_code=200,
            data=schemas.UserRoleResponseSchema.from_orm(db_user_role)
        )
    finally:
        db.close()

def delete_user_role(user_role: schemas.UserRoleDeleteSchema, db: Session):
    try:    
        db_user_role = db.query(models.UserRoleDB).filter(models.UserRoleDB.id == user_role.id).first()
        if db_user_role is None:
            raise HTTPException(status_code=404, detail="User role not found")
        db.delete(db_user_role)
        db.commit()
        return schemas.BaseResponseSchema(
            message="User role deleted successfully",
            status_code=200,
            data=schemas.UserRoleResponseSchema.from_orm(db_user_role)
        )
    finally:
        db.close() 