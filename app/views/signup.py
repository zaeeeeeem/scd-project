import tkinter as tk
from tkinter import messagebox
from app.services.auth import register_user  # 👈 import your logic

def signup_page():
    root = tk.Tk()
    root.title("Sign Up - Hospital System")
    root.geometry("500x500")

    def handle_register():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        user_role = user_type.get()

        success, msg = register_user(username, email, password, user_role)
        if success:
            messagebox.showinfo("Success", msg)
            root.destroy()
        else:
            messagebox.showerror("Error", msg)
            
    def open_login_page():
        root.destroy()
        from .login import login_page
        login_page()

    def go_back():
        root.destroy()

    tk.Label(root, text="Create Account", font=("Arial", 18, "bold")).pack(pady=40)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root, width=30)
    username_entry.pack()

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack()

    tk.Label(root, text="Register as", pady=10).pack()

    user_type = tk.StringVar(value="Patient")
    tk.Radiobutton(root, text="Doctor", variable=user_type, value="Doctor").pack()
    tk.Radiobutton(root, text="Patient", variable=user_type, value="Patient").pack()

    tk.Button(root, text="Register", width=20, command=handle_register).pack(pady=20)
    tk.Button(root, text="Login", command=open_login_page, width=20).pack()

    root.mainloop()
