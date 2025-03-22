from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime
from app.database import get_db
from app.users import views, schemas
from app.auth.views import get_current_user
from app.users.models import UserDB

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/users/", response_model=schemas.BaseResponseSchema)
def get_all_users(db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    return views.get_all_users(db)

@router.get("/users/{user_id}", response_model=schemas.BaseResponseSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    return views.get_user_by_id(user_id, db)

@router.post("/users/", response_model=schemas.BaseResponseSchema)
def create_user(
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    birth_date: Optional[datetime.datetime] = Form(None),
    is_active: bool = Form(True),
    user_type_id: int = Form(...),
    role_ids: List[int] = Form([]),
    password: str = Form(...),
    picture: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: UserDB = Depends(get_current_user)
):
    user_data = schemas.UserCreateSchema(
        email=email,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        is_active=is_active,
        user_type_id=user_type_id,
        role_ids=role_ids,
        password=password,
        picture=picture
    )
    return views.create_user(user_data, db)

@router.put("/users/", response_model=schemas.BaseResponseSchema)
def update_user(
    id: int = Form(...),
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    birth_date: Optional[datetime.datetime] = Form(None),
    is_active: bool = Form(True),
    user_type_id: int = Form(...),
    role_ids: List[int] = Form([]),
    password: Optional[str] = Form(None),
    picture: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: UserDB = Depends(get_current_user)
):
    user_data = schemas.UserUpdateSchema(
        id=id,
        email=email,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        is_active=is_active,
        user_type_id=user_type_id,
        role_ids=role_ids,
        password=password,
        picture=picture
    )
    return views.update_user(user_data, db)

@router.delete("/users/", response_model=schemas.BaseResponseSchema)
def delete_user(user: schemas.UserDeleteSchema, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    return views.delete_user(user, db) 