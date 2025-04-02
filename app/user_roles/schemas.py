import datetime
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any


class BaseSchema(BaseModel):
    id: int


class BaseResponseSchema(BaseModel):
    message: str
    status_code: int
    data: Optional[Any] = None


class UserRoleBaseSchema(BaseSchema):
    name: str


class UserRoleResponseSchema(UserRoleBaseSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class UserRoleCreateSchema(UserRoleBaseSchema):

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Kullanıcı tipi adı boş olamaz")
        if len(v) > 50:
            raise ValueError("Kullanıcı tipi adı 50 karakterden uzun olamaz")
        return v


class UserRoleUpdateSchema(UserRoleBaseSchema):

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Kullanıcı tipi adı boş olamaz")
        if len(v) > 50:
            raise ValueError("Kullanıcı tipi adı 50 karakterden uzun olamaz")
        return v


class UserRoleDeleteSchema(UserRoleBaseSchema):
    pass
