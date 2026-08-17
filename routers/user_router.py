from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.user_schema import UserRegisterRequest, UserResponse, UserLoginRequest, TokenResponse
from database import get_db
import services.user_service as user_service

router = APIRouter(
    prefix="/api",
    tags=["User"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register(user_in: UserRegisterRequest, db: Session = Depends(get_db)):
    return user_service.register_user(user_in, db)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLoginRequest, db: Session = Depends(get_db)):
    return {
        "message": "Đăng nhập thành công",
        "access_token": user_service.login_user(user, db),
        "token_type": "Bearer"
    }