"""Role service module for handling role-related operations."""
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.app.module.role.sql_role import SqlRole

class Role:
    """Service class for handling role-related operations."""

    def __init__(self):
        self.role_sql = SqlRole()

    def created_role(self, data):
        """
        Create a new role in the database.
        
        Validates required fields, checks for duplicate names,
        and inserts the role record into the database.
        """
        try:
            required = ["name", "descripcion"]
            if all(getattr(data, f) for f in required):
                if not self.role_sql.get_name_role(data.name):
                    data_role = data.dict()
                    sql_created = self.role_sql.sql_created_role(data_role)
                    if not sql_created:
                        return JSONResponse(content="Error Created Role", status_code=400)
                    return JSONResponse(content="Created Role", status_code=200)
                return JSONResponse(content="Duplicate Name", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error created role:" + str(e))
            raise HTTPException(status_code=500, detail="Error Created Role") from e

    def get_roles(self):
        """
        Retrieve all roles from the database.
        
        Fetches the complete roles list and converts created_at field to string format.
        """
        try:
            roles_list = []
            get_roles = self.role_sql.get_list_roles()
            for value in get_roles:
                if value.get('created_at'):
                    value['created_at'] = str(value['created_at'])
                roles_list.append(value)
            if roles_list:
                return JSONResponse(content=roles_list, status_code=200)
            return JSONResponse(content="No Data", status_code=200)
        except Exception as e:
            print("Role/get_roles: " + str(e))
            raise HTTPException(status_code=400, detail="Error Get Roles") from e

    def update_role(self, data):
        """
        Modify a role in the database.
        
        The role is identified by its ID.
        """
        try:
            required = ["id", "name", "descripcion"]
            if all(getattr(data, f) is not None for f in required):
                get_id = self.role_sql.get_id_role(data.id)
                if get_id:
                    data_role = data.dict()
                    update_role = self.role_sql.sql_update_role(data_role)
                    if not update_role:
                        return JSONResponse(content="Role Could Not Updated", status_code=400)
                    return JSONResponse(content="Update Role", status_code=200)
                return JSONResponse(content="Role Not Exist", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error Update role:" + str(e))
            raise HTTPException(status_code=500, detail="Error Update Role") from e

    def delete_role(self, role_id):
        """
        Delete a role from the database.
        """
        try:
            delete_role = self.role_sql.sql_delete_role(role_id)
            if not delete_role:
                return JSONResponse(content="Role Could Not Deleted", status_code=400)
            return JSONResponse(content="Delete Role", status_code=200)
        except Exception as e:
            print("Error Delete role:" + str(e))
            raise HTTPException(status_code=500, detail="Error Delete Role") from e
