from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, views

router = APIRouter()

@router.post("/login", response_model=schemas.TokenSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return views.login(db, form_data.username, form_data.password)
