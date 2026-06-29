"""
    This module contains the router for the permission endpoints.
    It uses the Permission class to handle the permission logic.
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.app.core.permissions import has_permission
from src.app.scheme.scheme import CreatePermissionSchema, UpdatePermissionSchema, DeletePermissionSchema
from src.app.module.permission.permission import Permission
from src.app.core.auth_service import get_current_user

appPermission = APIRouter(tags=["Permission"])

@appPermission.post("/created_permission")
async def created_permission(
    data: CreatePermissionSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint to create a new permission.
        It receives the permission data and returns the result of the creation process.
    """
    if has_permission(current_user["id"], "create_permission"):
        permission = Permission()
        result = permission.created_permission(data)
        return result
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appPermission.get("/get_permissions")
async def get_permissions(
    current_user=Depends(get_current_user)
):
    """
        Endpoint to get all permissions. It returns a list of all permissions.
    """
    if has_permission(current_user["id"], "view_permissions"):
        permission = Permission()
        return permission.get_permissions()
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appPermission.put("/update_permission")
async def update_permission(
    data: UpdatePermissionSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint for updating permissions; returns the updated permission
    """
    if has_permission(current_user["id"], "update_permission"):
        permission = Permission()
        return permission.update_permission(data)
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )

@appPermission.delete("/delete_permission")
async def delete_permission(
    data: DeletePermissionSchema,
    current_user=Depends(get_current_user)
):
    """
        Endpoint for deleting permissions; returns the deleted permission
    """
    if has_permission(current_user["id"], "delete_permission"):
        permission = Permission()
        return permission.delete_permission(data.id)
    return JSONResponse(
            content="You do not have permission to perform this action.",
            status_code=403
        )
