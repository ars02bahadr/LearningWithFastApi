import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class BaseModelDb(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

class UserTypeDB(BaseModelDb):
    __tablename__ = "user_types"
    name = Column(String, index=True) 
    users = relationship("UserDB", back_populates="user_type")