import tkinter as tk
from tkinter import messagebox
from app.views.doctor.profile import ProfilePage
from app.views.doctor.appointments import AppointmentPage
from app.views.doctor.medical_records import MedicalRecordsPage

class DoctorDashboard(tk.Toplevel):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.title("Doctor Dashboard")
        self.geometry("400x300")
        self.user = user  # user is a dictionary containing user info

        # tk.Label(self, text=f"Welcome Dr. {user.get('full_name', '')}", font=("Arial", 16)).pack(pady=20)
        #
        # # Button to Manage Profile
        # tk.Button(self, text="Manage Profile", width=25, command=self.open_profile).pack(pady=10)
        #
        # # Button to Manage Appointments
        # tk.Button(self, text="Manage Appointments", width=25, command=self.open_appointments).pack(pady=10)
        #
        # # Button to Manage Medical Records
        # tk.Button(self, text="Manage Medical Records", width=25, command=self.open_medical_records).pack(pady=10)

        tk.Button(self, text="Manage Profile", width=25, command=self.open_profile).pack(pady=10)
        tk.Button(self, text="Manage Appointments", width=25, command=self.open_appointments).pack(pady=10)
        tk.Button(self, text="Medical Records", width=25, command=self.open_medical_records).pack(pady=10)


        
        # Optional logout button
        tk.Button(self, text="Logout", width=25, command=self.logout).pack(pady=20)

    def open_profile(self):
        ProfilePage(self)

    def open_appointments(self):
        AppointmentPage(self)

    def open_medical_records(self):
        MedicalRecordsPage(self)

    def logout(self):
        self.destroy()
        #destroyed
