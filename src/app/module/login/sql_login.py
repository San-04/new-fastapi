from src.app.database.db import dataBase


class sqlLogin:
    def get_user(email):
        sql = """SELECT password FROM usuarios WHERE email = %s"""
        values = (email, )
        result = dataBase.mysqlExecute(sql, db="tienda_plus", values=values, fetch=True)
        return result