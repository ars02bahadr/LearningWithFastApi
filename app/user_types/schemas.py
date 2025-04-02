import datetime
from pydantic import BaseModel
from typing import Optional, Any

class BaseSchema(BaseModel):
    id: int

class BaseResponseSchema(BaseModel):
    message: str
    status_code: int
    data: Optional[Any] = None

from pydantic import Field, field_validator

class UserTypeBaseSchema(BaseSchema):
    id: int = Field(gt=0, description="ID must be greater than 0")
    name: str = Field(
        min_length=1,
        max_length=50,
        pattern=r'^[a-zA-Z0-9\s]+$'
    )

    @field_validator('id')
    @classmethod
    def validate_id(cls, v):
        if v <= 0:
            raise ValueError("ID sıfırdan büyük olmalıdır")
        return v

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Kullanıcı tipi adı boş olamaz")
        if len(v) > 50:
            raise ValueError("Kullanıcı tipi adı 50 karakterden uzun olamaz")
        return v

class UserTypeResponseSchema(UserTypeBaseSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True

class UserTypeCreateSchema(UserTypeBaseSchema):
    pass

class UserTypeUpdateSchema(UserTypeBaseSchema):
    pass

class UserTypeDeleteSchema(UserTypeBaseSchema):
    pass 