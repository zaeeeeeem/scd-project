import tkinter as tk
from tkinter import messagebox
from app.services.auth import login_user

def login_page(master, show_frame_callback):
    frame = tk.Frame(master)
    # frame.title("Login - Hospital System") # Frames don't have titles
    # frame.geometry("500x400") # Master controls geometry

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()

        success, result = login_user(email, password)

        if success:
            messagebox.showinfo("Success", f"Welcome {result['full_name']}!")
            # Pass the user data (result) to the dashboard
            show_frame_callback("dashboard", data=result)
        else:
            messagebox.showerror("Error", result)

    def open_signup_page_callback():
        # Instead of root.destroy() and direct call, use the callback
        show_frame_callback("signup")

    tk.Label(frame, text="Login to Hospital System", font=("Arial", 18, "bold")).pack(pady=40)

    tk.Label(frame, text="Email").pack()
    email_entry = tk.Entry(frame, width=30)
    email_entry.pack()

    tk.Label(frame, text="Password").pack()
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.pack()

    tk.Button(frame, text="Login", width=20, command=handle_login).pack(pady=20)
    tk.Button(frame, text="Sign Up", width=20, command=open_signup_page_callback).pack()

    return frame
