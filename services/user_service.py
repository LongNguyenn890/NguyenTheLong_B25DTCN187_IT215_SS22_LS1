from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.user_schema import UserRegisterRequest, UserLoginRequest
from models.user_model import UserModel
from security.password import generate_hashed_password, verify_password
from security.gen_jwt import generate_access_token


def register_user(user: UserRegisterRequest, db: Session):
    exitsting_username = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if exitsting_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tài khoản đã tồn tại"
        )
    
    new_user = UserModel(
        username = user.username,
        password = generate_hashed_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def login_user(user: UserLoginRequest, db: Session):
    user_db = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if user_db is None or not verify_password(user.password, user_db.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tài khoản và mật khẩu không đúng"
        )
        
    return generate_access_token(user_db.username)
        
    