"""
    This module contains the router for the user endpoints.
    It uses the User class to handle the user logic.
"""

from fastapi import APIRouter, Depends
from src.app.scheme.scheme import CreateUserSchema
from src.app.module.user.user import User
from src.app.core.auth_service import get_current_user

appUser = APIRouter(tags=["User"])

@appUser.post("/created_user")
async def created_user(
    data: CreateUserSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint to create a new user. 
        It receives the user data and returns the result of the creation process.
    """
    user = User()
    result = user.created_user(data)
    return result

@appUser.get("/get_users")
async def get_users(
    current_user=Depends(get_current_user)
):
    """Endpoint to get all users. It returns a list of all users."""
    user = User()
    return user.get_users()