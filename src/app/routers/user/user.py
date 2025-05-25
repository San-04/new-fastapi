from fastapi import APIRouter
from src.app.scheme.scheme import schemeCreatedUser
from src.app.module.user.user import user


appUser = APIRouter()

@appUser.post("/created_user")
async def created_user(data: schemeCreatedUser):
    result = user.createdUser(data)
    return result