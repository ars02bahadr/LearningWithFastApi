from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas
from app import get_db
from . import views

router = APIRouter()

@router.get("/get-all", response_model=schemas.BaseResponseSchema)
def get_all(db: Session = Depends(get_db)):
    return views.get_all_user_types(db)

@router.get("/get-by-id", response_model=schemas.BaseResponseSchema)
def get_by_id(user_type_id: int, db: Session = Depends(get_db)):
    return views.get_user_type_by_id(user_type_id, db)

@router.post("/create", response_model=schemas.BaseResponseSchema)
def create(user_type: schemas.UserTypeCreateSchema, db: Session = Depends(get_db)):
    return views.create_user_type(user_type, db)

@router.put("/update", response_model=schemas.BaseResponseSchema)
def update(user_type: schemas.UserTypeUpdateSchema, db: Session = Depends(get_db)):
    return views.update_user_type(user_type, db)

@router.delete("/delete", response_model=schemas.BaseResponseSchema)
def delete(user_type: schemas.UserTypeDeleteSchema, db: Session = Depends(get_db)):
    return views.delete_user_type(user_type, db) 