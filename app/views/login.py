import tkinter as tk
from tkinter import messagebox
from app.services.auth import login_user  # 👈 Make sure this path matches your structure
from app.views.doctor.dashboard import DoctorDashboard
from .Patient.dashboard import patient_dashboard
from .Admin.dashboard import admin_dashboard
from app.services.auth import login_user

def login_page():
    root = tk.Tk()
    root.title("Login - Hospital System")
    root.geometry("500x500")

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()

        success, result = login_user(email, password)

        if success:
            messagebox.showinfo("Success", f"Welcome {result['full_name']}!")

            if result['role_id'] == 1:
                messagebox.showinfo("Login", "Admin dashboard not yet implemented.")
            elif result['role_id'] == 2:
                root.withdraw()  # or root.withdraw() if you want to reopen login later
                DoctorDashboard(master=root, user=result)  # Pass user data if needed
            else:
                messagebox.showinfo("Login", "Patient dashboard not yet implemented.")
            # Example: redirect based on role
            if result['role_id'] == 1:
                patient_dashboard()
            elif result['role_id'] == 3:
                admin_dashboard()
            # else:
            #     open_patient_dashboard()
        else:
            messagebox.showerror("Error", result)

    def open_signup_page():
        root.destroy()
        from .signup import signup_page
        signup_page()

    tk.Label(root, text="Login to Hospital System", font=("Arial", 18, "bold")).pack(pady=40)

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack()

    tk.Button(root, text="Login", width=20, command=handle_login).pack(pady=20)
    tk.Button(root, text="Sign Up", width=20, command=open_signup_page).pack()

    root.mainloop()
