"""
Module for validating user authentication tokens.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.app.module.login.login import Login
from src.app.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Validate JWT token and retrieve the current authenticated user.
    """
    try:
        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )

        email = payload["sub"]
        instance_login = Login()
        current_user = instance_login.get_user(email)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")

        return current_user
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        ) from e
