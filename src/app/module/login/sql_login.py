from src.app.database.db import Database


class SqlLogin:

    def __init__(self):
        self.dataBase = Database()

    def getEmail(self, email):
        try:
            sql = f"""SELECT password FROM usuarios WHERE email = '{email}'"""
            result = self.dataBase.mysqlExecute(sql, 'tienda_plus')
            return result
        except Exception as e:
            print(f"Error occurred while fetching email: {e}")
            return None