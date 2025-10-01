from src.app.module.login.sql_login import SqlLogin
from src.app.core.security import verify_password, create_access_token
from fastapi.responses import JSONResponse

class Login:

    def __init__(self):
        self.loginSql = SqlLogin()

    def start_login(self, data):
        passwordUser = self.loginSql.get_user(data.email)
        if passwordUser:
            hashedPassword = passwordUser[0]['password']
            verifyPassword = verify_password(data.password, hashedPassword)
            if verifyPassword:
                accessToken = create_access_token({"sub": data.email})
                result = {
                    'username': data.email,
                    'token': accessToken,
                }
                return JSONResponse(content = result, status_code=200)
            else:
                return JSONResponse(content="invalid password", status_code=200)
        else:
            return JSONResponse(content="user not found", status_code=200)