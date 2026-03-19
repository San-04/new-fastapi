"""Database layer for user-related queries."""

from src.app.database.db import Database

class SqlUser:
    """Database layer for user-related queries."""

    def __init__(self):
        self.data_base = Database()

    def sql_created_user(self, data):
        """
        Insert a new user record into the database.
        
        Creates a new user entry in the usuario table with provided information.
        """
        sql = f"""INSERT INTO usuario
            (names, last_names, email, password, age, tele_phone, date_birth, role_id)
            VALUES ('{data['firstName']}', '{data['lastName']}',
            '{data['email']}', '{data['password']}', '{data['age']}',
            '{data['mobile']}', '{data['dateBirth']}', {data['role_id']})
        """
        result = self.data_base.msql_execute_insert(sql, 'tienda_plus')
        return result

    def get_email_user(self, email):
        """
        Check if a user with the given email exists in the database.
        """
        sql = f"""SELECT id FROM usuario WHERE email = '{email}'"""
        result = self.data_base.mysql_execute(sql, db="tienda_plus")
        return result

    def get_list_users(self):
        """
        Retrieve all user records from the database with pagination support.
        
        Fetches complete user information from the usuario table.
        Results are yielded for efficient memory usage with large datasets.
        """
        sql = """SELECT * FROM usuario"""
        result = self.data_base.mysql_execute_paginated(sql, db="tienda_plus")
        return result

    def sql_update_user(self, data):
        """
            Updates a user's information 
        """
        sql = f"""
            UPDATE usuario
            SET names = '{data['firstName']}',
                last_names = '{data['lastName']}',
                age = '{data['age']}',
                tele_phone = '{data['mobile']}',
                date_birth = '{data['dateBirth']}',
                status = '{data['status']}',
                role_id = '{data['role_id']}'
            WHERE id = '{data['id_user']}'
        """
        return self.data_base.msql_execute_update(sql, db="tienda_plus")
