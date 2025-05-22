import hashlib
from app.models import user
from app.views.doctor.dashboard import DoctorDashboard

def register_user(full_name, email, password, role_name):
    # Hash the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Get role ID
    role_id = user.get_role_id(role_name)
    if not role_id:
        return False, "Invalid role."

    # Insert into users table
    user_id = user.insert_user(role_id, full_name, email, password_hash)
    if not user_id:
        return False, "Email already exists."

    # Insert into specific role table
    if role_name.lower() == "patient":
        user.insert_patient(user_id)
    elif role_name.lower() == "doctor":
        user.insert_doctor(user_id)
    elif role_name.lower() == "admin":
        user.insert_admin(user_id)

    return True, "Registration successful."

##################################################################################

import hashlib
from app.models import user

def login_user(email, password):
    user_data = user.get_user_by_email(email)
    if not user_data:
        return False, "User not found."

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash != user_data['password']:
        return False, "Incorrect password."

    return True, user_data  # ✅ Return user data on success


def login_success(user):
    if user["role_id"] == get_role_id("Doctor"):
        app = DoctorDashboard(user)
        app.mainloop()
    elif user["role_id"] == get_role_id("Patient"):
        app = PatientDashboard(user)
        app.mainloop()
    else:
        messagebox.showerror("Error", "Unknown role.")
