"""
    This module contains the router for the login endpoint.
    It uses the Login class to handle the login logic.
"""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.app.module.login.login import Login

appLogin = APIRouter(prefix="/auth", tags=["Login"])

@appLogin.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login endpoint that receives the login form data and returns the access token."""
    instance_login = Login()
    return instance_login.start_login(form_data)
