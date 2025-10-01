from src.app.module.login.login import Login
from fastapi import APIRouter
from src.app.scheme.scheme import schemeLogin

appLogin = APIRouter()

@appLogin.post("/login")
async def start_login(data: schemeLogin):
    login = Login()
    data = login.start_login(data)
    return data