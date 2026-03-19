"""User service module for handling user-related operations."""

import traceback
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.app.module.user.sql_user import SqlUser
from src.app.core.security import get_password_hash

class User:
    """Service class for handling user-related operations."""

    def __init__(self):
        self.user_sql = SqlUser()

    def created_user(self, data):
        """
        Create a new user in the database.
        
        Validates required fields, checks for duplicate emails, hashes the password,
        and inserts the user record into the database.
        """
        try:
            required = [
                "firstName", "lastName", "email", "password",
                "age", "dateBirth", "role_id"
            ]
            if all(getattr(data, f) for f in required):
                if not self.user_sql.get_email_user(data.email):
                    data_user = data.dict()
                    password = get_password_hash(data.password)
                    data_user['password'] = password
                    sql_created = self.user_sql.sql_created_user(data_user)
                    if not sql_created:
                        return JSONResponse(content="Error Created User", status_code=400)
                    return JSONResponse(content="Created User", status_code=200)
                return JSONResponse(content="Duplicate Email", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error created user:" + str(e))
            raise HTTPException(status_code=500, detail="Error Created User") from e

    def get_users(self):
        """
        Retrieve all users from the database.
        
        Fetches the complete user list and removes sensitive information (passwords).
        Converts fecha_nacimiento field to string format.
        """
        try:
            users_list = []
            get_users = self.user_sql.get_list_users()
            for value in get_users:
                value['date_birth'] = str(value['date_birth'])
                value.pop("password", None)
                users_list.append(value)
            if users_list:
                return JSONResponse(content=users_list, status_code=200)
            return JSONResponse(content="No Data", status_code=200)
        except Exception as e:
            print("User/get_users: " + str(e))
            raise HTTPException(status_code=400, detail="Error Get Users") from e

    def update_user(self, data):
        """
            Modify a user in the database

            The user is identified by their email address to retrieve the database ID
        """
        try:
            required = [
                "firstName", "lastName", "email",
                "age", "dateBirth", "role_id", "status", "mobile"
            ]
            if all(getattr(data, f) for f in required):
                get_email = self.user_sql.get_email_user(data.email)
                if get_email:
                    data_user = data.dict()
                    data_user['id_user'] = get_email[0]['id']
                    update_user = self.user_sql.sql_update_user(data_user)
                    if not update_user:
                        return JSONResponse(content="User Could Not Updated", status_code=400)
                    return JSONResponse(content="Update User", status_code=200)
                return JSONResponse(content="Email Not Exist", status_code=200)
            return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error Update user:" + str(e))
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Error Update User") from e
