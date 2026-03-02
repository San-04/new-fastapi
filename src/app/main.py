"""
    This module contains the main application of the project.
    It imports the routers and includes them in the FastAPI app.
"""

from fastapi import FastAPI
from src.app.routers.login import login
from src.app.routers.user import user

app = FastAPI()
app.include_router(login.appLogin)
app.include_router(user.appUser)
