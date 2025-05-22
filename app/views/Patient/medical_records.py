import tkinter as tk
from tkinter import ttk

class MedicalRecordsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Medical Records", font=("Arial", 14, "bold")).pack(pady=10)

        # Treeview for tabular records
        columns = ("name", "email", "department", "bill")
        tree = ttk.Treeview(self, columns=columns, show="headings")

        # Define headings
        tree.heading("name", text="Name")
        tree.heading("email", text="Email")
        tree.heading("department", text="Department")
        tree.heading("bill", text="Bill")

        # Define column widths
        tree.column("name", width=100)
        tree.column("email", width=150)
        tree.column("department", width=120)
        tree.column("bill", width=80)

        # Insert dummy records
        dummy_data = [
            ("Usama", "usama@example.com", "Cardiology", "$1000"),
            ("Ali", "ali@example.com", "Orthopedics", "$750"),
            ("Sara", "sara@example.com", "ENT", "$500")
        ]
        for record in dummy_data:
            tree.insert("", tk.END, values=record)

        tree.pack(pady=10)

        tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=10)
