# src/app/core/auth_service.py
from src.app.module.login.sql_login import SqlLogin
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.app.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

    username = payload["sub"]
    user_model = SqlLogin()
    current_user = user_model.get_user(username)
    if not current_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return current_user
