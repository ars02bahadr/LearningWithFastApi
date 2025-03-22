import datetime
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, Any, List
from fastapi import File, UploadFile, Form

from app.user_roles.schemas import UserRoleResponseSchema
from app.user_types.schemas import UserTypeResponseSchema

class BaseSchema(BaseModel):
    id: int

class BaseResponseSchema(BaseModel):
    message: str
    status_code: int
    data: Optional[Any] = None

class UserBaseSchema(BaseSchema):
    email: EmailStr
    first_name: str
    last_name: str
    birth_date: Optional[datetime.datetime] = None
    is_active: bool = True
    user_type_id: int
    role_ids: List[int] = []

class UserResponseSchema(UserBaseSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_type: UserTypeResponseSchema
    roles: List[UserRoleResponseSchema]
    picture: Optional[str] = None

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    email: EmailStr = Form(...)
    first_name: str = Form(...)
    last_name: str = Form(...)
    birth_date: Optional[datetime.datetime] = Form(None)
    is_active: bool = Form(True)
    user_type_id: int = Form(...)
    role_ids: List[int] = Form([])
    password: str = Form(...)
    picture: Optional[UploadFile] = File(None)

class UserUpdateSchema(BaseModel):
    id: int = Form(...)
    email: EmailStr = Form(...)
    first_name: str = Form(...)
    last_name: str = Form(...)
    birth_date: Optional[datetime.datetime] = Form(None)
    is_active: bool = Form(True)
    user_type_id: int = Form(...)
    role_ids: List[int] = Form([])
    password: Optional[str] = Form(None)
    picture: Optional[UploadFile] = File(None)

class UserDeleteSchema(UserBaseSchema):
    pass 