"""Permission service module for handling permission-related operations."""

import traceback
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.app.module.permission.sql_permission import SqlPermission

class Permission:
    """Service class for handling permission-related operations."""

    def __init__(self):
        self.permission_sql = SqlPermission()

    def created_permission(self, data):
        """
        Create a new permission in the database.
        
        Validates required fields, checks for duplicate names,
        inserts the permission record, and assigns it to specified roles.
        """
        try:
            required = ["name", "descripcion"]
            if all(getattr(data, f) is not None for f in required):
                if not self.permission_sql.get_name_permission(data.name):
                    data_perm = data.dict()
                    data_perm.pop('role_ids', None)
                    sql_created = self.permission_sql.sql_created_permission(data_perm)
                    if not sql_created:
                        return JSONResponse(content="Error Created Permission", status_code=400)
                    if hasattr(data, 'role_ids') and data.role_ids:
                        get_perm = self.permission_sql.get_name_permission(data.name)
                        if get_perm:
                            new_id = get_perm[0]['id']
                            for role_id in data.role_ids:
                                self.permission_sql.sql_assign_permission_to_role(role_id, new_id)
                    return JSONResponse(content="Created Permission", status_code=200)
                return JSONResponse(content="Duplicate Name", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error created permission:" + str(e))
            raise HTTPException(status_code=500, detail="Error Created Permission") from e

    def get_permissions(self):
        """
        Retrieve all permissions from the database.
        
        Fetches the complete permissions list and converts created_at field to string format.
        """
        try:
            permissions_list = []
            get_perms = self.permission_sql.get_list_permissions()
            for value in get_perms:
                if value.get('created_at'):
                    value['created_at'] = str(value['created_at'])
                permissions_list.append(value)
            if permissions_list:
                return JSONResponse(content=permissions_list, status_code=200)
            return JSONResponse(content="No Data", status_code=200)
        except Exception as e:
            print("Permission/get_permissions: " + str(e))
            raise HTTPException(status_code=400, detail="Error Get Permissions") from e

    def update_permission(self, data):
        """
        Modify a permission in the database.
        
        The permission is identified by its ID, and its role associations are synced.
        """
        try:
            required = ["id", "name", "descripcion"]
            if all(getattr(data, f) is not None for f in required):
                get_id = self.permission_sql.get_id_permission(data.id)
                if get_id:
                    data_perm = data.dict()
                    data_perm.pop('role_ids', None)
                    update_perm = self.permission_sql.sql_update_permission(data_perm)
                    if not update_perm:
                        return JSONResponse(content="Permission Could Not Updated", status_code=400)
                    
                    # Sync role mappings
                    if hasattr(data, 'role_ids'):
                        current_mappings = self.permission_sql.sql_get_permission_roles(data.id)
                        current_role_ids = [m['role_id'] for m in current_mappings] if current_mappings else []
                        
                        # Remove roles not in the new list
                        for role_id in current_role_ids:
                            if role_id not in data.role_ids:
                                self.permission_sql.sql_remove_permission_from_role(role_id, data.id)
                                
                        # Add new roles in the list
                        for role_id in data.role_ids:
                            if role_id not in current_role_ids:
                                self.permission_sql.sql_assign_permission_to_role(role_id, data.id)
                                
                    return JSONResponse(content="Update Permission", status_code=200)
                return JSONResponse(content="Permission Not Exist", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error Update permission:" + str(e))
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Error Update Permission") from e

    def delete_permission(self, permission_id):
        """
        Delete a permission from the database.
        Clears associated role relationships first to maintain DB integrity.
        """
        try:
            # Delete intermediate child records first
            self.permission_sql.sql_delete_all_permission_roles(permission_id)
            
            # Delete parent record
            delete_perm = self.permission_sql.sql_delete_permission(permission_id)
            if not delete_perm:
                return JSONResponse(content="Permission Could Not Deleted", status_code=400)
            return JSONResponse(content="Delete Permission", status_code=200)
        except Exception as e:
            print("Error Delete permission:" + str(e))
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Error Delete Permission") from e
