import tkinter as tk

class AppointmentPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Book Appointment", font=("Arial", 14, "bold")).pack(pady=10)

        # Patient Name
        tk.Label(self, text="Patient Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Age
        tk.Label(self, text="Age").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        # Department Dropdown
        tk.Label(self, text="Department").pack()
        self.department_var = tk.StringVar()
        self.department_var.set("Select")
        departments = ["Cardiology", "Neurology", "Dermatology", "Orthopedics"]
        tk.OptionMenu(self, self.department_var, *departments).pack()

        # Doctor Dropdown
        tk.Label(self, text="Doctor").pack()
        self.doctor_var = tk.StringVar()
        self.doctor_var.set("Select")
        doctors = ["Dr. Ahsan", "Dr. Fatima", "Dr. Usama", "Dr. Iqra"]
        tk.OptionMenu(self, self.doctor_var, *doctors).pack()

        # Submit Button
        tk.Button(self, text="Submit",width=17, command=self.submit_appointment).pack(pady=10)

        # Back Button
        tk.Button(self, text="Back",width=17, command=lambda: controller.show_frame("MainMenu")).pack(pady=10)

    def submit_appointment(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        department = self.department_var.get()
        doctor = self.doctor_var.get()

        print("---- Appointment Details ----")
        print(f"Patient Name: {name}")
        print(f"Age: {age}")
        print(f"Department: {department}")
        print(f"Doctor: {doctor}")
        print("------------------------------")
