from pydantic import BaseModel, EmailStr

class CreateUserSchema(BaseModel):
    """
        Schema for creating a new user.
    """
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    age: int
    mobile: str
    dateBirth: str
    role_id: int

class UpdateUserSchema(BaseModel):
    """
        Schema for update user.
    """
    firstName: str
    lastName: str
    email: EmailStr
    age: int
    mobile: str
    dateBirth: str
    role_id: int
