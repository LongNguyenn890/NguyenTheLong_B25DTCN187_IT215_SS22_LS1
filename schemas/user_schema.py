from pydantic import BaseModel, ConfigDict, Field

class UserRegisterSchema(BaseModel):
    username: str = Field(..., min_length=4, max_length=50)
    password: str = Field(..., min_length=8)
    

class UserResponse(BaseModel):
    id: int
    username: str
    
    model_config = ConfigDict(from_attributes=True)