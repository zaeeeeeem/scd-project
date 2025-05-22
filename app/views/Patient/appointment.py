import tkinter as tk

class AppointmentPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Book Appointment").pack(pady=10)

        tk.Label(self, text="Patient Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Age").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Select Doctor / Department").pack()
        self.doctor_entry = tk.Entry(self)
        self.doctor_entry.pack()

        tk.Label(self, text="Reason for Visit").pack()
        self.reason_entry = tk.Entry(self)
        self.reason_entry.pack()

        tk.Button(self, text="Submit", command=self.book_appointment).pack(pady=10)

        tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu")).pack()

    def book_appointment(self):
        # Placeholder for saving logic
        print("Appointment booked (simulation)")
