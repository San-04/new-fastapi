from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.app.module.login.login import Login

appLogin = APIRouter(prefix="/auth", tags=["Login"])

@appLogin.post("/login")
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    instanceLogin = Login()
    return instanceLogin.startLogin(formData)