from fastapi import APIRouter
from src.app.scheme.scheme import schemeCreatedUser
from src.app.module.user.user import User
from src.app.core.security import decode_access_token
from fastapi.responses import JSONResponse


appUser = APIRouter()

@appUser.post("/created_user")
async def created_user(data: schemeCreatedUser):
    decodeToken = decode_access_token(data.token)
    if decodeToken and decodeToken['sub']:
        user = User()
        result = user.createdUser(data)
        return result
    else:
        return JSONResponse(content="invalidToken", status_code=401)