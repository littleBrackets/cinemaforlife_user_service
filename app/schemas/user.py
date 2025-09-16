from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
