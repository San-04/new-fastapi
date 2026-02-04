from src.app.module.user.sql_user import SqlUser
from src.app.core.security import get_password_hash
from fastapi.responses import JSONResponse

class User: 

    def __init__(self):
        self.userSql = SqlUser()

    def createdUser(self, data):
        try:
            if data.firtName and data.lastName and data.email and data.password and data.age:
                if not self.userSql.getEmailUser(data.email):
                    dataUser = data.dict()
                    password = get_password_hash(data.password)
                    dataUser['password'] = password
                    sqlCreated = self.userSql.sqlCreatedUser(dataUser)
                    if not sqlCreated:
                        return JSONResponse(content="Error Created User", status_code=400)
                    return JSONResponse(content="Created User", status_code=200)
                else:
                    return JSONResponse(content="Duplicate Email", status_code=200)
            else: 
                return JSONResponse(content="Missing Parameters", status_code=200)
        except Exception as e:
            print("Error created user:" + str(e))
            return JSONResponse(content="Error Created User", status_code=400)
        
    def getUsers(self):
        try:
            usersList = []
            gettUsers = self.userSql.getListUsers() 
            if gettUsers:
                for value in gettUsers:
                    value['fechaNacimiento'] = str(value['fechaNacimiento'])
                    value.pop("password", None)
                    usersList.append(value)
                return JSONResponse(content=usersList, status_code=200)
            else:
                return JSONResponse(content="No Data", status_code=200)
        except Exception as e:
            print("User/getUsers: " + str(e))
            return JSONResponse(content="Error Get Users", status_code=400)