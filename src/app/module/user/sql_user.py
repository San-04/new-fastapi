from src.app.database.db import dataBase

class sqlUser:
    def sqlCreatedUser(data):
        sql = """INSERT INTO usuarios (nombre, apellido, email, password, edad) 
                VALUES (%s, %s, %s, %s, %s)"""
        
        values = ( data['firtName'], data['lastName'], data['email'], data['password'], data['age'] )

        result = dataBase.mysqlExecute(sql, 'tienda_plus', values=values)
        return result
    
    def getEmailUser(email):
        sql = """SELECT email FROM usuarios WHERE email = %s"""
        values = (email,)
        result = dataBase.mysqlExecute(sql, db="tienda_plus", values=values, fetch=True)
        return result

