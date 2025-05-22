import tkinter as tk
from .patient_management import PatientManagementPage
from .doctor_management import DoctorManagementPage
from .medical_records import MedicalRecordsPage

class AdminDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Dashboard")
        self.geometry("500x500")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (MainMenu, PatientManagementPage, DoctorManagementPage, MedicalRecordsPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)

        def backToLogin():
            from ..login import login_page
            login_page()

        tk.Button(self, text="Patient Management", width=25, command=lambda: controller.show_frame("PatientManagementPage")).pack(pady=10)
        tk.Button(self, text="Doctor Management", width=25, command=lambda: controller.show_frame("DoctorManagementPage")).pack(pady=10)
        tk.Button(self, text="Medical Records", width=25, command=lambda: controller.show_frame("MedicalRecordsPage")).pack(pady=10)
        tk.Button(self, text="Logout", width=25, command=backToLogin).pack(pady=10)


def admin_dashboard():
        app = AdminDashboard()
        app.mainloop()
