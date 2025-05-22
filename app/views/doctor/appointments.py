import tkinter as tk

class AppointmentPage(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Manage Appointments")
        self.geometry("400x300")

        tk.Label(self, text="Appointments Management", font=("Arial", 16, "bold")).pack(pady=20)

        # Static placeholder appointment list
        appointments = [
            "2025-05-25 10:00 AM - Patient: Alice Smith",
            "2025-05-26 02:00 PM - Patient: Bob Johnson",
            "2025-05-27 11:30 AM - Patient: Carol Lee",
        ]

        for appt in appointments:
            tk.Label(self, text=appt).pack(pady=3)
