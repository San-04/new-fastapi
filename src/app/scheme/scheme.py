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
