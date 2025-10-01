from src.app.core.config import Settings
import mysql.connector

class Database:

    def __init__(self):
        self.settings = Settings()

    def conexion(self, db):
        conn = mysql.connector.connect(
            user = self.settings.USER_BD,
            password = self.settings.PASSWORD_BD,
            host = self.settings.HOST_BD,
            port = self.settings.PORT_BD,
            database = db
        )
        return conn

#    def mysqlExecute(self, sql: str, db: str, values: tuple = None, fetch: bool = False):
#        conn = None
#        try:
#            conn = self.conexion(db)
#            cur = conn.cursor(dictionary=True)
#            if values:
#                cur.execute(sql, values)
#            else:
#                cur.execute(sql)
#
#            if fetch:
#                result = list(cur.fetchall())
#            else:
#                conn.commit()
#                result = {"success": True}
#
#            cur.close()
#            conn.close()
#            return result
#
#        except Exception as e:
#            if conn:
#                conn.close()
#            print("Error connection mysql:", e)
#            return {"success": False, "error": str(e)}
        
    def mysqlExecutePaginated(self, sql: str, db: str, pageSize: int = 1000):
        try:
            conn = self.conexion(db)
            cur = conn.cursor(dictionary=True)
            cur.execute(sql)
            while True:
                rows = cur.fetchmany(pageSize)
                if not rows:
                    break
                yield from rows
        except Exception as e:
            print("Database/mysqlExecutePaginated" + str(e))
        finally:
            cur.close()
            conn.close()

    def mysqlExecute(self, sql: str, db: str):
        try:
            conn = self.conexion(db)
            cur = conn.cursor(dictionary=True)
            cur.execute(sql)
            return [cur.fetchall()]
        except Exception as e:
            print("Database/mysqlExecute" + str(e))
        finally:
            cur.close()
            conn.close()
    
    def msqlExecuteInsert(self, sql, db):
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print("Database/msqlExecuteInsert" + str(e))
            return False
        finally:
            cur.close()
            conn.close()

    def msqlExecuteUpdate(self, sql, db):
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            cur.commit()
            return True
        except Exception as e:
            print("Database/msqlExecuteUpdate" + str(e))
            return False
        finally:
            cur.close()
            conn.close()

    def msqlExecuteDeleted(self, sql, db):
        try:
            conn = self.conexion(db)
            cur = conn.cursor()
            cur.execute(sql)
            cur.commit()
            return True
        except Exception as e:
            print("Database/msqlExecuteDeleted" + str(e))
            return False
        finally:
            cur.close()
            conn.close()
