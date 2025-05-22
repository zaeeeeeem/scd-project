import tkinter as tk

class MedicalRecordsPage(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Medical Records")
        self.geometry("400x300")

        tk.Label(self, text="Medical Records", font=("Arial", 16, "bold")).pack(pady=20)

        # Static example medical records
        records = [
            "Record #1: Blood Test - Normal",
            "Record #2: X-Ray - Minor fracture",
            "Record #3: Allergy Test - Negative",
        ]

        for rec in records:
            tk.Label(self, text=rec).pack(pady=3)
