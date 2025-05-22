import tkinter as tk
from views.login import login_page
from views.signup import signup_page

def open_login_page():
    root.destroy()
    login_page()

def open_signup_page():
    root.destroy()
    signup_page()

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("500x500")

tk.Label(root, text="Hospital Management System", font=("Arial", 20)).pack(pady=10)

tk.Button(root, text="Login", command=open_login_page, width=30).pack(pady=5)
tk.Button(root, text="Sign Up", command=open_signup_page, width=30).pack(pady=5)

root.mainloop()






# import mysql.connector
# from mysql.connector import Error
#
# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         database="HMS",
#         user="root",
#         password=""
#     )
#
#     if conn.is_connected():
#         db_version = conn.server_info
#         print(f"Connected to MySQL Server version: ", db_version)
#         cursor = conn.cursor()
#         cursor.execute("SELECT DATABASE();")
#         record = cursor.fetchone()
#         print("Connected to MySQL server", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
#
# finally:
#     if conn and conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("Connected to MySQL server", record)