from fastapi import FastAPI
from app.user_types.routes import router as user_types_router
from app.user_roles.routes import router as user_roles_router
from app.users.routes import router as users_router
from app.auth.routes import router as auth_router

app = FastAPI()

# Router'ları ekle
app.include_router(user_types_router, prefix="/user-types", tags=["user-types"])
app.include_router(user_roles_router, prefix="/user-roles", tags=["user-roles"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
