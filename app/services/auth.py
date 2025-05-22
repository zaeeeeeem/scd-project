import hashlib
from app.models import user

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
