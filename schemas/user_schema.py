from pydantic import BaseModel, ConfigDict, Field

class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=4, max_length=50)
    password: str = Field(..., min_length=8)
    
    
class UserLoginRequest(BaseModel):
    username: str
    password: str
    

class UserResponse(BaseModel):
    id: int
    username: str
    
    model_config = ConfigDict(from_attributes=True)
    

class TokenResponse(BaseModel):
    message: str
    access_token: str
    token_type: str