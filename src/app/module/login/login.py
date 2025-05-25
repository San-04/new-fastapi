from src.app.module.login.sql_login import sqlLogin
from fastapi.responses import JSONResponse

class login:
    def start_login(data):
        email = data.email
        password = data.password
        sql_login = sqlLogin.login_user(email, password)
        if sql_login:
            return JSONResponse(content=sql_login, status_code=200)
        else:
            return JSONResponse(content="user not found", status_code=200)