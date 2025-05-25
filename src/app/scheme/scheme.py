from pydantic import BaseModel

class schemeLogin(BaseModel):
    email: str
    password: str


class schemeCreatedUser(BaseModel):
    firtName: str
    lastName: str
    email: str
    password: str
    age: int