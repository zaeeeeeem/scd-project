import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',         # Replace if your MySQL has a password
        db='hms',  # Replace with your actual DB name
        cursorclass=pymysql.cursors.DictCursor
    )
