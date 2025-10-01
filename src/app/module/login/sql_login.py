from src.app.database.db import Database


class SqlLogin:

    def __init__(self):
        self.dataBase = Database()

    def get_user(self, email):
        sql = f"""SELECT password FROM usuarios WHERE email = '{email}'"""
        result = self.dataBase.mysqlExecute(sql, 'tienda_plus')
        return result