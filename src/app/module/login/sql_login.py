"""Database layer for login-related queries."""

from src.app.database.db import Database

class SqlLogin:
    """Database layer for login-related queries."""

    def __init__(self):
        self.data_base = Database()

    def get_email(self, email):
        """
        Retrieve user password hash by email address.
        
        Queries the database for a user with the specified email and returns
        their password hash for authentication verification.
        """
        sql = f"""SELECT id, password FROM usuario WHERE email = '{email}'"""
        result = self.data_base.mysql_execute(sql, 'tienda_plus')
        return result
