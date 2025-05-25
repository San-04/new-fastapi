from src.app.routers.login import login
from src.app.routers.user import user
from fastapi import FastAPI




app = FastAPI()
app.include_router(login.appLogin, tags=["Login"])
app.include_router(user.appUser, tags=["User"])

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a mi API con FastAPI"}

