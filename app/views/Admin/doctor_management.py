# doctor_management.py
import tkinter as tk
from tkinter import Frame


class DoctorManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Doctor Management", font=("Arial", 16)).pack(pady=10)

        def backToDashboard():
            from .dashboard import admin_dashboard
            admin_dashboard()

        doctors = [
            {"name": "Dr. House", "specialty": "Diagnostics"},
            {"name": "Dr. Watson", "specialty": "General Physician"},
            {"name": "Dr. Grey", "specialty": "Surgery"},
        ]

        for doctor in doctors:
            tk.Label(self, text=f"Name: {doctor['name']}, Specialty: {doctor['specialty']}").pack(pady=2)

        tk.Button(self, text="Back", width=20, command=backToDashboard).pack(pady=20)