from src.app.module.login.login import login
from fastapi import APIRouter
from src.app.scheme.scheme import schemeLogin

appLogin = APIRouter()

@appLogin.post("/login")
async def start_login(data: schemeLogin):
    data = login.start_login(data)
    return data