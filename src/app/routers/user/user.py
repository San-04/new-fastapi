from fastapi import APIRouter, Depends
from src.app.scheme.scheme import schemeCreatedUser
from src.app.module.user.user import User
from src.app.core.auth_service import get_current_user

appUser = APIRouter()

@appUser.post("/created_user")
async def created_user(
    data: schemeCreatedUser,
    current_user=Depends(get_current_user)
):
    user = User()
    result = user.createdUser(data)
    return result