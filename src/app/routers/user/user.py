from fastapi import APIRouter, Depends
from src.app.scheme.scheme import schemeCreatedUser
from src.app.module.user.user import User
from src.app.core.auth_service import getCurrentUser

appUser = APIRouter(tags=["User"])

@appUser.post("/created_user")
async def createdUser(
    data: schemeCreatedUser,
    current_user=Depends(getCurrentUser)
):
    user = User()
    result = user.createdUser(data)
    return result