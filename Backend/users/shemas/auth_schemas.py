from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    user_name : str = Field(alias="userName")
    email : EmailStr
    password : str

class LoginSchema(BaseModel):
    email : EmailStr
    password : str

class LoginGoogle(BaseModel):
    token:str