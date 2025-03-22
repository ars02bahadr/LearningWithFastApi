from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine
from app.user_types.models import UserTypeDB
from app.user_roles.models import UserRoleDB
from app.users.models import UserDB
from app.users.routes import router as users_router
from app.auth.routes import router as auth_router

app = FastAPI()

# Statik dosyaları servis et
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

# Router'ları ekle
app.include_router(auth_router, prefix="/api")
app.include_router(users_router, prefix="/api") 