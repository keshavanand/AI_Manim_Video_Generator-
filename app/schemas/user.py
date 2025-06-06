# Pydantic schemas for user registration/auth
from pydantic import BaseModel

class Register_user(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User_Data(BaseModel):
    username: str
    email: str | None = None