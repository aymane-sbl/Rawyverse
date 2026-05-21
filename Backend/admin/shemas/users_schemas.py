from pydantic import BaseModel, EmailStr


class AdminUsersSchema(BaseModel):
    email: EmailStr