import tkinter as tk

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Patient Profile").pack(pady=10)

        # Simulated fields (patient_id and user_id will be auto-generated from DB - not shown here)
        tk.Label(self, text="Age").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Gender").pack()
        self.gender_entry = tk.Entry(self)
        self.gender_entry.pack()

        tk.Label(self, text="Contact Number").pack()
        self.contact_entry = tk.Entry(self)
        self.contact_entry.pack()

        tk.Label(self, text="Address").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        tk.Button(self, text="Save Profile",width=17, command=self.save_profile).pack(pady=10)

        tk.Button(self, text="Back", width=17,command=lambda: controller.show_frame("MainMenu")).pack()

    def save_profile(self):
        # Placeholder function
        print("Profile saved (simulation)")
