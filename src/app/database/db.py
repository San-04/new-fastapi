from src.app.core.config import settings
import mysql.connector

class dataBase:
    @staticmethod
    def mysqlExecute(sql: str, db: str, values: tuple = None, fetch: bool = False):
        conn = None
        try:
            conn = mysql.connector.connect(
                user=settings.USER_BD,
                password=settings.PASSWORD_BD,
                host=settings.HOST_BD,
                port=settings.PORT_BD,
                database=db
            )
            cur = conn.cursor(dictionary=True)

            if values:
                cur.execute(sql, values)
            else:
                cur.execute(sql)

            if fetch:
                result = list(cur.fetchall())
            else:
                conn.commit()
                result = {"success": True}

            cur.close()
            conn.close()
            return result

        except Exception as e:
            if conn:
                conn.close()
            print("Error connection mysql:", e)
            return {"success": False, "error": str(e)}
