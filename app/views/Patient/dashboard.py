import tkinter as tk
from appointment import AppointmentPage
from medical_records import MedicalRecordsPage
from profile import ProfilePage

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient Dashboard")
        self.geometry("400x400")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (MainMenu, ProfilePage, AppointmentPage, MedicalRecordsPage):
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

        tk.Label(self, text="Patient Dashboard").pack(pady=20)

        tk.Button(self, text="Profile",width=17, command=lambda: controller.show_frame("ProfilePage")).pack(pady=10)
        tk.Button(self, text="Book Appointment",width=17, command=lambda: controller.show_frame("AppointmentPage")).pack(pady=10)
        tk.Button(self, text="View Medical Records",width=17, command=lambda: controller.show_frame("MedicalRecordsPage")).pack(pady=10)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
