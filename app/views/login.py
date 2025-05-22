import tkinter as tk

def login_page():
    root = tk.Tk()
    root.title("Login - Hospital System")
    root.geometry("500x500")

    def open_signup_page():
        root.destroy()
        from .signup import signup_page
        signup_page()

    tk.Label(root, text="Login", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=10)

    tk.Label(root, text="Password",).pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack()

    tk.Button(root, text="Login", width=20).pack(pady=20)
    tk.Button(root, text="SignUp", command=open_signup_page, width=20).pack()

    root.mainloop()
