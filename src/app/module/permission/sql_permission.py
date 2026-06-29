"""Database layer for permission-related queries."""

from src.app.database.db import Database

class SqlPermission:
    """Database layer for permission-related queries."""

    def __init__(self):
        self.data_base = Database()

    def sql_created_permission(self, data):
        """
        Insert a new permission record into the database.
        
        Creates a new entry in the permissions table with provided information.
        Sets the creation date using MySQL's UTC_TIMESTAMP() to keep it in UTC.
        """
        sql = f"""INSERT INTO permissions
            (name, descriptions, created_at)
            VALUES ('{data['name']}', '{data['descripcion']}', UTC_TIMESTAMP())
        """
        result = self.data_base.msql_execute_insert(sql, 'tienda_plus')
        return result

    def get_name_permission(self, name):
        """
        Check if a permission with the given name exists in the database.
        """
        sql = f"""SELECT id FROM permissions WHERE name = '{name}'"""
        result = self.data_base.mysql_execute(sql, db="tienda_plus")
        return result

    def get_id_permission(self, permission_id):
        """
        Check if a permission with the given ID exists in the database.
        """
        sql = f"""SELECT id FROM permissions WHERE id = {permission_id}"""
        result = self.data_base.mysql_execute(sql, db="tienda_plus")
        return result

    def get_list_permissions(self):
        """
        Retrieve all permission records from the database with pagination support.
        """
        sql = """SELECT * FROM permissions"""
        result = self.data_base.mysql_execute_paginated(sql, db="tienda_plus")
        return result

    def sql_update_permission(self, data):
        """
        Updates a permission's name and description.
        Does not touch the created_at field.
        """
        sql = f"""
            UPDATE permissions
            SET name = '{data['name']}',
                descriptions = '{data['descripcion']}'
            WHERE id = {data['id']}
        """
        return self.data_base.msql_execute_update(sql, db="tienda_plus")

    def sql_delete_permission(self, permission_id):
        """
        Deletes a permission from the database.
        """
        sql = f"""
            DELETE FROM permissions
            WHERE id = {permission_id}
        """
        return self.data_base.mysql_execute_delete(sql, db="tienda_plus")

    def sql_assign_permission_to_role(self, role_id, permission_id):
        """
        Assign a permission to a role in the role_permissions intermediate table.
        """
        sql = f"""INSERT INTO role_permissions (role_id, permission_id)
            VALUES ({role_id}, {permission_id})
        """
        return self.data_base.msql_execute_insert(sql, 'tienda_plus')

    def sql_get_permission_roles(self, permission_id):
        """
        Get all role IDs associated with a permission.
        """
        sql = f"""SELECT role_id FROM role_permissions WHERE permission_id = {permission_id}"""
        return self.data_base.mysql_execute(sql, db="tienda_plus")

    def sql_remove_permission_from_role(self, role_id, permission_id):
        """
        Remove the association of a permission from a specific role.
        """
        sql = f"""DELETE FROM role_permissions
            WHERE role_id = {role_id} AND permission_id = {permission_id}
        """
        return self.data_base.mysql_execute_delete(sql, db="tienda_plus")

    def sql_delete_all_permission_roles(self, permission_id):
        """
        Remove all role associations for a permission.
        """
        sql = f"""DELETE FROM role_permissions
            WHERE permission_id = {permission_id}
        """
        return self.data_base.mysql_execute_delete(sql, db="tienda_plus")
