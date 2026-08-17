from fastapi import FastAPI

from database import Base, engine
from models.user_model import UserModel
from routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API ĐĂNG KÍ & ĐĂNG NHẬP",
    summary="Dùng để đăng kí và đăng nhập tài khoản người dùng",
    version="1.0.0"
)

app.include_router(user_router)