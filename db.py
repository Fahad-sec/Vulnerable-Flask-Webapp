import pymysql

def get_db_connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="vulnuser",
            password="vulnpass",
            database="vulnwebapp",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None 



