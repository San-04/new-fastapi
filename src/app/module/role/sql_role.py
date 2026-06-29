"""Database layer for role-related queries."""

from src.app.database.db import Database

class SqlRole:
    """Database layer for role-related queries."""

    def __init__(self):
        self.data_base = Database()

    def sql_created_role(self, data):
        """
        Insert a new role record into the database.
        
        Creates a new role entry in the roles table with provided information.
        Sets the creation date using MySQL's UTC_TIMESTAMP() to keep it in UTC.
        """
        sql = f"""INSERT INTO roles
            (name, description, created_at)
            VALUES ('{data['name']}', '{data['descripcion']}', UTC_TIMESTAMP())
        """
        result = self.data_base.msql_execute_insert(sql, 'tienda_plus')
        return result

    def get_name_role(self, name):
        """
        Check if a role with the given name exists in the database.
        """
        sql = f"""SELECT id FROM roles WHERE name = '{name}'"""
        result = self.data_base.mysql_execute(sql, db="tienda_plus")
        return result

    def get_id_role(self, role_id):
        """
        Check if a role with the given ID exists in the database.
        """
        sql = f"""SELECT id FROM roles WHERE id = {role_id}"""
        result = self.data_base.mysql_execute(sql, db="tienda_plus")
        return result

    def get_list_roles(self):
        """
        Retrieve all role records from the database with pagination support.
        """
        sql = """SELECT * FROM roles"""
        result = self.data_base.mysql_execute_paginated(sql, db="tienda_plus")
        return result

    def sql_update_role(self, data):
        """
        Updates a role's information (name and description).
        Does not touch the created_at field.
        """
        sql = f"""
            UPDATE roles
            SET name = '{data['name']}',
                description = '{data['descripcion']}'
            WHERE id = {data['id']}
        """
        return self.data_base.msql_execute_update(sql, db="tienda_plus")

    def sql_delete_role(self, role_id):
        """
        Deletes a role from the database.
        """
        sql = f"""
            DELETE FROM roles
            WHERE id = {role_id}
        """
        return self.data_base.mysql_execute_delete(sql, db="tienda_plus")
