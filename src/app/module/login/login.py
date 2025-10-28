from src.app.module.login.sql_login import SqlLogin
from src.app.core.security import verify_password, create_access_token
from fastapi import HTTPException

class Login:

    def __init__(self):
        self.loginSql = SqlLogin()

    def startLogin(self, formData):
        try:
            user_data = self.loginSql.getEmail(formData.username)
        
            if not user_data:
                raise HTTPException(status_code=401, detail="User not found")
            
            hashed_password = user_data[0]["password"]
            if not verify_password(formData.password, hashed_password):
                raise HTTPException(status_code=401, detail="Incorrect password")

            token = create_access_token({"sub": formData.username})
            return {"access_token": token, "token_type": "bearer"}
        except Exception as e:
            print(f"Error occurred during login: {e}")
            return {"error": "Login failed"}
    
    def getUser(self, email):
        try:
            user_data = self.loginSql.getEmail(email)
            if not user_data:
                return None
            return user_data[0]
        except Exception as e:
            print(f"Error occurred while fetching user: {e}")
            return None
