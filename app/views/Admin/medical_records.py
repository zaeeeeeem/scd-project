# medical_records.py
import tkinter as tk

class MedicalRecordsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Medical Records", font=("Arial", 16)).pack(pady=10)

        def backToDashboard():
            from .dashboard import admin_dashboard
            admin_dashboard()

        records = [
            {"patient": "John Doe", "diagnosis": "Flu", "treatment": "Rest and hydration"},
            {"patient": "Jane Smith", "diagnosis": "Allergy", "treatment": "Antihistamines"},
            {"patient": "Alice Brown", "diagnosis": "Diabetes", "treatment": "Insulin therapy"},
        ]

        for record in records:
            tk.Label(self, text=f"Patient: {record['patient']}, Diagnosis: {record['diagnosis']}, Treatment: {record['treatment']}").pack(pady=2)

        tk.Button(self, text="Back", width=20, command=backToDashboard).pack(pady=20)
