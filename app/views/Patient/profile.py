import tkinter as tk

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Patient Profile", font=("Arial", 14, "bold")).pack(pady=10)



        # Gender with OptionMenu
        tk.Label(self, text="Gender").pack()
        self.gender_var = tk.StringVar()
        self.gender_var.set("Select")
        tk.OptionMenu(self, self.gender_var, "Male", "Female", "Other").pack()

        # Contact Number
        tk.Label(self, text="Contact Number").pack()
        self.contact_entry = tk.Entry(self)
        self.contact_entry.pack()

        # Address
        tk.Label(self, text="Address").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        # Submit Button
        tk.Button(self, text="Submit",width=17, command=self.submit_data).pack(pady=10)

        # Back Button
        tk.Button(self, text="Back",width=17, command=lambda: controller.show_frame("MainMenu")).pack(pady=10)

    def submit_data(self):

        gender = self.gender_var.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()

        # Show data in console
        print("---- Patient Profile ----")

        print(f"Gender: {gender}")
        print(f"Contact Number: {contact}")
        print(f"Address: {address}")
        print("--------------------------")
