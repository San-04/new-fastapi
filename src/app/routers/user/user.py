"""
    This module contains the router for the user endpoints.
    It uses the User class to handle the user logic.
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.app.core.permissions import has_permission
from src.app.scheme.scheme import CreateUserSchema, UpdateUserSchema
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
    if has_permission(current_user["id"], "create_user"):
        user = User()
        result = user.created_user(data)
        return result
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appUser.get("/get_users")
async def get_users(
    current_user=Depends(get_current_user)
):
    """
        Endpoint to get all users. It returns a list of all users.
    """
    if has_permission(current_user["id"], "view_users"):
        user = User()
        return user.get_users()
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appUser.put("/update_user")
async def update_user(
    data: UpdateUserSchema,
    current_user = Depends(get_current_user)
):
    """
        Endpoint for updating users; returns the updated user
    """
    if has_permission(current_user['id'], 'update_user'):
        user = User()
        return user.update_user(data)
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )
