from src.app.module.user.sql_user import SqlUser
from src.app.core.security import get_password_hash
from fastapi.responses import JSONResponse

class User: 

    def __init__(self):
        self.user_sql = SqlUser()

    def createdUser(self, data):
        try:
            if data.firtName and data.lastName and data.email and data.password and data.age:
                if not self.user_sql.getEmailUser(data.email):
                    dataUser = data.dict()
                    password = get_password_hash(data.password)
                    dataUser['password'] = password
                    print("name", dataUser)
                    sqlCreated = self.user_sql.sqlCreatedUser(dataUser)
                    print("holis result", sqlCreated)
                    if not sqlCreated:
                        return JSONResponse(content="error created user", status_code=400)
                    return JSONResponse(content="created user", status_code=200)
                else:
                    return JSONResponse(content="duplicate email", status_code=200)
            else: 
                return JSONResponse(content="missing parameters", status_code=200)
        except Exception as e:
            print("error created user", e)
            return JSONResponse(content="error created user", status_code=400)