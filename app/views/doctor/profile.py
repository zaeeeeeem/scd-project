import tkinter as tk

class ProfilePage(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Doctor Profile")
        self.geometry("400x300")

        tk.Label(self, text="Doctor Profile Page", font=("Arial", 16, "bold")).pack(pady=20)

        # Sample static data - you will replace this with real DB data later
        tk.Label(self, text="Name: Dr. John Doe").pack(pady=5)
        tk.Label(self, text="Specialization: Cardiology").pack(pady=5)
        tk.Label(self, text="Qualification: MBBS, MD").pack(pady=5)
        tk.Label(self, text="Contact: 123-456-7890").pack(pady=5)
        tk.Label(self, text="Availability: Mon-Fri 9AM - 5PM").pack(pady=5)
