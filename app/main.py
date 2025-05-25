import tkinter as tk
from app.views.login import login_page
from app.views.signup import signup_page
from app.views.dashboard import dashboard_page

class App:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Hospital Management System")
        self.root.geometry("600x500") # Adjusted size for better layout
        
        # Optional: Add a main title label if desired, or handle titles within frames
        # tk.Label(self.root, text="Hospital Management System", font=("Arial", 20)).pack(pady=10)

        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.current_user_data = None # To store user data after login
        self.current_page_name = None # To store the name of the current page
        
        # Store page constructors (the functions themselves)
        self.pages = {
            "login": login_page,
            "signup": signup_page,
            "dashboard": dashboard_page
        }
        
        self.show_frame("login")

    def show_frame(self, page_name, data=None):
        self.current_page_name = page_name # Update current page name

        if page_name == "dashboard":
            if data: # Data passed, typically from login
                self.current_user_data = data
            elif not self.current_user_data: # No data passed and no existing user data
                print("Error: No user data for dashboard, redirecting to login.")
                self.show_frame("login") # Redirect to login
                return # Stop further execution for this call
        elif page_name == "login": # Clear user data on logout/going to login
            self.current_user_data = None

        # Clear previous frame's content
        for widget in self.main_container.winfo_children():
            widget.destroy()
            
        page_constructor = self.pages.get(page_name)
        if page_constructor:
            frame = None
            if page_name == "dashboard":
                # Ensure current_user_data is available (it should be due to checks above)
                if self.current_user_data:
                    frame = page_constructor(self.main_container, self.show_frame, self.current_user_data)
                else:
                    # This case should ideally be caught by the redirect above, but as a fallback:
                    print("Error: Dashboard accessed without user data. Redirecting to login.")
                    self.show_frame("login")
                    return
            else: # For login and signup pages
                frame = page_constructor(self.main_container, self.show_frame)
            
            if frame:
                frame.pack(fill=tk.BOTH, expand=True)
        else:
            print(f"Error: Page '{page_name}' not found.")
            # Optionally, show an error page or go to a default page
            # For now, just printing an error.

def main():
    root = tk.Tk()
    app = App(root) # Create an instance of the App class
    root.mainloop()

if __name__ == "__main__":
    main()






# import mysql.connector
# from mysql.connector import Error
#
# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         database="HMS",
#         user="root",
#         password=""
#     )
#
#     if conn.is_connected():
#         db_version = conn.server_info
#         print(f"Connected to MySQL Server version: ", db_version)
#         cursor = conn.cursor()
#         cursor.execute("SELECT DATABASE();")
#         record = cursor.fetchone()
#         print("Connected to MySQL server", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
#
# finally:
#     if conn and conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("Connected to MySQL server", record)