from app import get_db_connection
import pymysql

def get_role_id(role_name):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT role_id FROM roles WHERE LOWER(role_name) = %s", (role_name.lower(),))
            result = cursor.fetchone()
            return result['role_id'] if result else None
    finally:
        conn.close()


def insert_user(role_id, full_name, email, password_hash):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (role_id, full_name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (role_id, full_name, email, password_hash))
            conn.commit()
            return cursor.lastrowid
    except pymysql.IntegrityError:
        return None
    finally:
        conn.close()

def insert_patient(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO patients (user_id) VALUES (%s)", (user_id,))
            conn.commit()
    finally:
        conn.close()

def insert_doctor(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO doctors (user_id) VALUES (%s)", (user_id,))
            conn.commit()
    finally:
        conn.close()

def insert_admin(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO admins (user_id) VALUES (%s)", (user_id,))
            conn.commit()
    finally:
        conn.close()
