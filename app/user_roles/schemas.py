import datetime
from pydantic import BaseModel
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
    pass

class UserRoleUpdateSchema(UserRoleBaseSchema):
    pass

class UserRoleDeleteSchema(UserRoleBaseSchema):
    pass 