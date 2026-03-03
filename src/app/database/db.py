"""Database connection and execution utilities."""

import traceback
import mysql.connector
from src.app.core.config import Settings

class Database:
    """
    Database connection manager for MySQL operations.
    
    Handles database connections and provides methods for executing various
    SQL operations (SELECT, INSERT, UPDATE, DELETE) with proper error handling
    and resource cleanup.
    """
    def __init__(self):
        """
        Initialize the Database instance with application settings.
        """
        self.settings = Settings()

    def conexion(self, db):
        """
        Establish a MySQL database connection.
        
        Creates and returns a new MySQL connection using credentials from the
        application settings. Each connection is independent and should be closed
        after use.
        """
        conn=mysql.connector.connect(
            user=self.settings.user_bd,
            password=self.settings.password_bd,
            host=self.settings.host_bd,
            port=self.settings.port_bd,
            database=db
        )
        return conn

    def mysql_execute_paginated(self, sql: str, db: str, page_size: int = 1000):
        """
        Execute a SELECT query and return results with pagination (generator).
        
        Efficiently fetches large result sets by yielding rows in batches,
        reducing memory consumption. Useful for processing large datasets.
        """
        try:
            conn = self.conexion(db)
            cur = conn.cursor(dictionary=True)
            cur.execute(sql)
            while True:
                rows = cur.fetchmany(page_size)
                if not rows:
                    break
                yield from rows
        except mysql.connector.Error as e:
            # Log properly instead of print in production
            traceback.print_exc()
            print(f"Database/mysql_execute_paginated: {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def mysql_execute(self, sql: str, db: str):
        """
        Execute a SELECT query and return all results.
        
        Fetches all matching rows from the database at once.
        Best used for queries expected to return a moderate number of rows.
        """
        try:

            conn = self.conexion(db)
            cur = conn.cursor(dictionary=True)
            cur.execute(sql)
            return cur.fetchall()
        except mysql.connector.Error as e:
            # Log properly instead of print in production
            traceback.print_exc()
            print(f"Database/mysql_execute: {e}")
            return []
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def msql_execute_insert(self, sql, db):
        """
        Execute an INSERT query to add new records to the database.
        
        Inserts one or more rows into a table and commits the transaction.
        """
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            return True
        except mysql.connector.Error as e:
            # Log properly instead of print in production
            traceback.print_exc()
            print(f"Database/msql_execute_insert: {e}")
            return False
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    def msql_execute_update(self, sql, db):
        """
        Execute an UPDATE query to modify existing records.
        
        Updates one or more rows in a table and commits the transaction.
        """
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            cur.commit()
            return True
        except mysql.connector.Error as e:
            # Log properly instead of print in production
            traceback.print_exc()
            print(f"Database/msql_execute_update: {e}")
            return False
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def mysql_execute_delete(self, sql, db):
        """
        Execute a DELETE query to remove records from the database.
        
        Deletes one or more rows from a table and commits the transaction.
        """
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            cur.commit()
            return True
        except mysql.connector.Error as e:
            # Log properly instead of print in production
            traceback.print_exc()
            print(f"Database/mysql_execute_delete: {e}")
            return False
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
