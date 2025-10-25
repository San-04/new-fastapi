from pydantic import BaseModel, EmailStr

class schemeLogin(BaseModel):
    email: EmailStr
    password: str


class schemeCreatedUser(BaseModel):
    firtName: str
    lastName: str
    email: EmailStr
    password: str
    age: int
