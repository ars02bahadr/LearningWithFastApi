import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from app.database import Base
from app.user_roles.models import UserRoleDB

class BaseModelDb(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

user_roles_users = Table(
    "user_roles_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("user_roles.id"), primary_key=True)
)

class UserDB(BaseModelDb):
    __tablename__ = "users"
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    picture = Column(String)
    birth_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    user_type_id = Column(Integer, ForeignKey("user_types.id"))
    user_type = relationship("UserTypeDB", back_populates="users")
    roles = relationship(UserRoleDB, secondary=user_roles_users, back_populates="users")

