import tkinter as tk

class MedicalRecordsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Medical Records", font=("Arial", 14, "bold")).pack(pady=10)

        # Container for table
        table_frame = tk.Frame(self)
        table_frame.pack()

        # Table Headers
        headers = ["Name", "Age", "Department", "Doctor"]
        for col, header in enumerate(headers):
            label = tk.Label(table_frame, text=header, width=15, borderwidth=1, relief="solid", anchor="center")
            label.grid(row=0, column=col)

        # Sample records
        self.records = [
            {"name": "Ali", "age": "30", "department": "Cardiology", "doctor": "Dr. Ahsan"},
            {"name": "Sara", "age": "25", "department": "Dermatology", "doctor": "Dr. Fatima"},
            {"name": "Usman", "age": "40", "department": "Neurology", "doctor": "Dr. Usama"},
        ]

        # Show data in rows
        for row_num, record in enumerate(self.records, start=1):
            tk.Label(table_frame, text=record["name"], width=15, borderwidth=1, relief="solid").grid(row=row_num, column=0)
            tk.Label(table_frame, text=record["age"], width=15, borderwidth=1, relief="solid").grid(row=row_num, column=1)
            tk.Label(table_frame, text=record["department"], width=15, borderwidth=1, relief="solid").grid(row=row_num, column=2)
            tk.Label(table_frame, text=record["doctor"], width=15, borderwidth=1, relief="solid").grid(row=row_num, column=3)

            # Print to console
            print("---- Record ----")
            print(f"Name: {record['name']}")
            print(f"Age: {record['age']}")
            print(f"Department: {record['department']}")
            print(f"Doctor: {record['doctor']}")
            print("----------------")

        # Back Button
        tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu")).pack(pady=10)
