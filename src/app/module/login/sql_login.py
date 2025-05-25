from src.app.database.db import dataBase


class sqlLogin:
    def login_user(email, password):
        sql = """SELECT * FROM usuarios WHERE email = %s AND password = %s"""
        values = (email, password,)
        result = dataBase.mysqlExecute(sql, db="tienda_plus", values=values, fetch=True)
        return result