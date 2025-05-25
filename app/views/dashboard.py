import tkinter as tk

def dashboard_page(master, show_frame_callback, user_data):
    """
    Creates the user dashboard page.

    Args:
        master: The parent Tkinter widget.
        show_frame_callback: Function to switch frames.
        user_data: Dictionary containing user information (e.g., {'full_name': 'John Doe'}).
    """
    frame = tk.Frame(master)
    frame.pack(fill="both", expand=True) # Make the frame fill the container

    # Display Welcome Message
    welcome_message = f"Welcome, {user_data.get('full_name', 'User')}!"
    tk.Label(frame, text=welcome_message, font=("Arial", 18)).pack(pady=20)

    # Add other dashboard elements here (e.g., view appointments, profile settings)
    tk.Label(frame, text="This is your dashboard. More features coming soon!", font=("Arial", 12)).pack(pady=10)

    # Logout Button
    logout_button = tk.Button(frame, text="Logout", command=lambda: show_frame_callback("login"))
    logout_button.pack(pady=20)

    return frame
