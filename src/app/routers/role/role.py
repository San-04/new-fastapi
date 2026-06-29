"""
    This module contains the router for the role endpoints.
    It uses the Role class to handle the role logic.
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.app.core.permissions import has_permission
from src.app.scheme.scheme import CreateRoleSchema, UpdateRoleSchema, DeleteRoleSchema
from src.app.module.role.role import Role
from src.app.core.auth_service import get_current_user

appRole = APIRouter(tags=["Role"])

@appRole.post("/created_role")
async def created_role(
    data: CreateRoleSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint to create a new role.
        It receives the role data and returns the result of the creation process.
    """
    if has_permission(current_user["id"], "create_role"):
        role = Role()
        result = role.created_role(data)
        return result
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appRole.get("/get_roles")
async def get_roles(
    current_user=Depends(get_current_user)
):
    """
        Endpoint to get all roles. It returns a list of all roles.
    """
    if has_permission(current_user["id"], "view_roles"):
        role = Role()
        return role.get_roles()
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appRole.put("/update_role")
async def update_role(
    data: UpdateRoleSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint for updating roles; returns the updated role
    """
    if has_permission(current_user["id"], "update_role"):
        role = Role()
        return role.update_role(data)
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appRole.delete("/delete_role")
async def delete_role(
    data: DeleteRoleSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint for deleting roles; returns the deleted role
    """
    if has_permission(current_user["id"], "delete_role"):
        role = Role()
        return role.delete_role(data.id)
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )
