# src/app/core/auth_service.py
from src.app.module.login.login import Login
from src.app.module.login.sql_login import SqlLogin
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.app.core.security import decode_access_token

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def getCurrentUser(token: str = Depends(oauth2Scheme)):
    try:
        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )

        email = payload["sub"]
        instanceLogin = Login()
        current_user = instanceLogin.getUser(email)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")

        return current_user
    except Exception as e:
        print(f"Error occurred while fetching current user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
