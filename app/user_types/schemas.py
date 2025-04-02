import datetime
from pydantic import BaseModel
from typing import Optional, Any

class BaseSchema(BaseModel):
    id: int

class BaseResponseSchema(BaseModel):
    message: str
    status_code: int
    data: Optional[Any] = None

from pydantic import Field, constr

class UserTypeBaseSchema(BaseSchema):
    id: int = Field(
        gt=0,
        description="ID must be greater than 0",
        error_messages={"gt": "ID sıfırdan büyük olmalıdır"}
    )
    name: constr(
        min_length=1,
        max_length=50,
        strip_whitespace=True,
        error_messages={
            "min_length": "Kullanıcı tipi adı boş olamaz",
            "max_length": "Kullanıcı tipi adı 50 karakterden uzun olamaz"
        }
    )

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