# patient_management.py
import tkinter as tk

class PatientManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Patient Management", font=("Arial", 16)).pack(pady=10)

        def backToDashboard():
            from .dashboard import admin_dashboard
            admin_dashboard()

        patients = [
            {"name": "John Doe", "age": 30, "gender": "Male"},
            {"name": "Jane Smith", "age": 25, "gender": "Female"},
            {"name": "Alice Brown", "age": 40, "gender": "Female"},
        ]

        for patient in patients:
            tk.Label(self, text=f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}").pack(pady=2)

        tk.Button(self, text="Back", width=20, command=backToDashboard).pack(pady=20)
