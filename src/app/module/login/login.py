"""Service layer for login-related operations."""

import traceback

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.app.module.login.sql_login import SqlLogin
from src.app.core.security import verify_password, create_access_token

class Login:
    """Service class for handling user login operations."""

    def __init__(self):
        self.login_sql = SqlLogin()

    def start_login(self, form_data):
        """
        Authenticate a user and generate an access token.
        
        Verifies the provided username and password against the database,
        and returns a JWT token if authentication is successful.
        """
        try:
            print("Starting login process for user:", form_data.username)
            user_data = self.login_sql.get_email(form_data.username)
            print("User data retrieved from database:", user_data)
            if not user_data:
                return JSONResponse(content="User not found", status_code=401)
            hashed_password = user_data[0]["password"]
            if not verify_password(form_data.password, hashed_password):
                return JSONResponse(content="Incorrect password", status_code=401)
            token = create_access_token({"sub": form_data.username})
            return JSONResponse(content={"access_token": token, "token_type": "bearer"}, status_code=200)
        except Exception as e:
            print("Error occurred during login:")
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Internal server error") from e

    def get_user(self, email):
        """
        Retrieve user information by email address.
        """
        user_data = self.login_sql.get_email(email)
        if not user_data:
            return None
        return user_data[0]
