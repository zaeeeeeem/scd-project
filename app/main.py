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