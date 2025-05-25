import tkinter as tk
from tkinter import messagebox
from app.services.auth import register_user

def signup_page(master, show_frame_callback):
    frame = tk.Frame(master)
    # frame.title("Sign Up - Hospital System") # Frames don't have titles
    # frame.geometry("500x500") # Master controls geometry

    def handle_register():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        user_role = user_type.get()

        success, msg = register_user(username, email, password, user_role)
        if success:
            messagebox.showinfo("Success", msg)
            # Instead of root.destroy() and direct call, use the callback
            show_frame_callback("login")
        else:
            messagebox.showerror("Error", msg)
            
    def open_login_page_callback():
        # Instead of root.destroy() and direct call, use the callback
        show_frame_callback("login")

    # The go_back function is redundant if it just goes to login, 
    # open_login_page_callback serves the same purpose.
    # If go_back was intended for a different "previous" page, its logic would need to be different.
    # For now, it's removed as open_login_page_callback covers the "back to login" scenario.

    tk.Label(frame, text="Create Account", font=("Arial", 18, "bold")).pack(pady=40)

    tk.Label(frame, text="Username").pack()
    username_entry = tk.Entry(frame, width=30)
    username_entry.pack()

    tk.Label(frame, text="Email").pack()
    email_entry = tk.Entry(frame, width=30)
    email_entry.pack()

    tk.Label(frame, text="Password").pack()
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.pack()

    tk.Label(frame, text="Register as", pady=10).pack()

    user_type = tk.StringVar(value="Patient") # Consider setting master for StringVar if needed in complex scenarios
    tk.Radiobutton(frame, text="Doctor", variable=user_type, value="Doctor").pack()
    tk.Radiobutton(frame, text="Patient", variable=user_type, value="Patient").pack()

    tk.Button(frame, text="Register", width=20, command=handle_register).pack(pady=20)
    tk.Button(frame, text="Login", command=open_login_page_callback, width=20).pack()

    return frame
