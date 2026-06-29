"""
    This module contains the main application of the project.
    It imports the routers and includes them in the FastAPI app.
"""

from fastapi import FastAPI
from src.app.routers.login import login
from src.app.routers.user import user
from src.app.routers.role import role
from src.app.routers.permission import permission

app = FastAPI()
app.include_router(login.appLogin)
app.include_router(user.appUser)
app.include_router(role.appRole)
app.include_router(permission.appPermission)
