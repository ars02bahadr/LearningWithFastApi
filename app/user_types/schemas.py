import datetime
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any


class BaseSchema(BaseModel):
    id: int


class BaseResponseSchema(BaseModel):
    message: str
    status_code: int
    data: Optional[Any] = None


class UserTypeBaseSchema(BaseSchema):
    name: str


class UserTypeResponseSchema(UserTypeBaseSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class UserTypeCreateSchema(UserTypeBaseSchema):

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Kullanıcı tipi adı boş olamaz")
        if len(v) > 50:
            raise ValueError("Kullanıcı tipi adı 50 karakterden uzun olamaz")
        return v


class UserTypeUpdateSchema(UserTypeBaseSchema):

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Kullanıcı tipi adı boş olamaz")
        if len(v) > 50:
            raise ValueError("Kullanıcı tipi adı 50 karakterden uzun olamaz")
        return v


class UserTypeDeleteSchema(UserTypeBaseSchema):
    pass
