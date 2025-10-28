from src.app.routers.login import login
from src.app.routers.user import user
from fastapi import FastAPI

app = FastAPI()
app.include_router(login.appLogin)
app.include_router(user.appUser)

