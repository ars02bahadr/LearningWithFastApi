import datetime
from pydantic import BaseModel
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
    pass

class UserTypeUpdateSchema(UserTypeBaseSchema):
    pass

class UserTypeDeleteSchema(UserTypeBaseSchema):
    pass 