from src.app.database.db import Database

class SqlUser:

    def __init__(self):
        self.database = Database()

    def sqlCreatedUser(self, data):
        try:
            sql = f"""INSERT INTO usuarios (nombre, apellido, email, password, edad) 
                VALUES '{data['firtName']}', '{data['lastName']}', '{data['email']}', '{data['password']}', '{data['age']}')
            """
            result = self.database.msqlExecuteInsert(sql, 'tienda_plus',)
            return result
        except Exception as e:
            print("SqlUser/sqlCreatedUser" + str(e))
    
    def getEmailUser(self, email):
        try:
            sql = f"""SELECT email FROM usuarios WHERE email = '{email}'"""
            result = self.database.mysqlExecute(sql, db="tienda_plus")
            return result
        except Exception as e:
            print("SqlUser/getEmailUser" + str(e))

