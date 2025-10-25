from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.app.module.login.sql_login import SqlLogin
from src.app.core.security import verify_password, create_access_token

appLogin = APIRouter(prefix="/auth", tags=["Login"])

@appLogin.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    login_instance = SqlLogin()
    user_data = login_instance.get_user(form_data.username)
    
    if not user_data:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    hashed_password = user_data[0]["password"]
    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
