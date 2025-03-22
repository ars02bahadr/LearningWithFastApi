from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas
from app import get_db
from . import views

router = APIRouter()

@router.get("/get-all", response_model=schemas.BaseResponseSchema)
def get_all(db: Session = Depends(get_db)):
    return views.get_all_user_roles(db)

@router.get("/get-by-id", response_model=schemas.BaseResponseSchema)
def get_by_id(user_role_id: int, db: Session = Depends(get_db)):
    return views.get_user_role_by_id(user_role_id, db)

@router.post("/create", response_model=schemas.BaseResponseSchema)
def create(user_role: schemas.UserRoleCreateSchema, db: Session = Depends(get_db)):
    return views.create_user_role(user_role, db)

@router.put("/update", response_model=schemas.BaseResponseSchema)
def update(user_role: schemas.UserRoleUpdateSchema, db: Session = Depends(get_db)):
    return views.update_user_role(user_role, db)

@router.delete("/delete", response_model=schemas.BaseResponseSchema)
def delete(user_role: schemas.UserRoleDeleteSchema, db: Session = Depends(get_db)):
    return views.delete_user_role(user_role, db) 