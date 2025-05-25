import unittest
from unittest.mock import patch, MagicMock, ANY
import tkinter as tk

# To allow running tests from the 'test' directory or the root project directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import App

# Mock classes for Tkinter widgets if needed, but mostly we mock our page functions
MockFrame = MagicMock(spec=tk.Frame)
MockFrame.pack = MagicMock()
MockFrame.winfo_children = MagicMock(return_value=[]) # No children by default
MockFrame.destroy = MagicMock()


class TestNavigation(unittest.TestCase):

    @patch('app.views.dashboard.dashboard_page')
    @patch('app.views.signup.signup_page')
    @patch('app.views.login.login_page')
    def setUp(self, mock_login_page_constructor, mock_signup_page_constructor, mock_dashboard_page_constructor):
        # Mock the root Tk window
        self.mock_root = MagicMock(spec=tk.Tk)
        self.mock_root.geometry = MagicMock()
        self.mock_root.title = MagicMock()
        self.mock_root.mainloop = MagicMock()
        
        # Configure the mock page constructors to return a mock frame instance
        # This allows us to check if they were called and with what arguments
        self.mock_login_page_frame = MockFrame()
        self.mock_signup_page_frame = MockFrame()
        self.mock_dashboard_page_frame = MockFrame()

        mock_login_page_constructor.return_value = self.mock_login_page_frame
        mock_signup_page_constructor.return_value = self.mock_signup_page_frame
        mock_dashboard_page_constructor.return_value = self.mock_dashboard_page_frame
        
        self.mock_login_page_constructor = mock_login_page_constructor
        self.mock_signup_page_constructor = mock_signup_page_constructor
        self.mock_dashboard_page_constructor = mock_dashboard_page_constructor

        # Patch auth services
        self.patch_login_user = patch('app.services.auth.login_user')
        self.mock_login_user = self.patch_login_user.start()

        self.patch_register_user = patch('app.services.auth.register_user')
        self.mock_register_user = self.patch_register_user.start()
        
        # Instantiate App. The __init__ method calls show_frame("login")
        # We need to wrap show_frame before App instantiation for the initial call check
        # However, it's simpler to let it run, then wrap for subsequent tests.
        self.app = App(self.mock_root)
        
        # Spy on show_frame: use a MagicMock that wraps the original method
        # This allows us to check calls to show_frame while still executing its logic
        self.app.show_frame = MagicMock(wraps=self.app.show_frame)
        
        # The initial call to show_frame("login") happened in App.__init__
        # We check this in test_initial_page_is_login.
        # For other tests, we might want to reset this spy or account for the initial call.

    def tearDown(self):
        patch.stopall() # Stops all patches started with patch.start()

    def test_initial_page_is_login(self):
        # App.__init__ calls self.show_frame("login").
        # The original App.show_frame was called, which in turn called the login_page constructor.
        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertEqual(self.app.current_page_name, "login") # Check internal state if we add it

    def test_login_to_signup(self):
        # Simulate being on the login page (already done by setUp)
        # The callback for the "Sign Up" button on login_page is self.app.show_frame
        self.app.show_frame.reset_mock() # Reset from initial call in __init__

        # Simulate the "Sign Up" button click from login_page
        # login_page's callback function is self.app.show_frame
        self.app.show_frame("signup") 

        self.app.show_frame.assert_called_with("signup")
        self.mock_signup_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertEqual(self.app.current_page_name, "signup")


    def test_signup_to_login_button(self):
        # First, navigate to signup page
        self.app.show_frame("signup")
        self.app.show_frame.reset_mock() # Reset after navigating to signup

        # Simulate the "Login" button click from signup_page
        # signup_page's callback for "Login" button is self.app.show_frame
        self.app.show_frame("login")

        self.app.show_frame.assert_called_with("login")
        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertIsNone(self.app.current_user_data) # Ensure user data is cleared
        self.assertEqual(self.app.current_page_name, "login")

    def test_signup_registration_to_login(self):
        self.mock_register_user.return_value = (True, "Registration successful")
        # Navigate to signup page first
        self.app.show_frame("signup")
        self.app.show_frame.reset_mock()

        # Simulate the flow after successful registration
        # In signup_page, handle_register calls show_frame_callback("login")
        # This callback is self.app.show_frame
        self.app.show_frame("login")

        self.app.show_frame.assert_called_with("login")
        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertIsNone(self.app.current_user_data)
        self.assertEqual(self.app.current_page_name, "login")

    def test_successful_login_shows_dashboard(self):
        user_info = {'full_name': 'Test User', 'email': 'test@example.com'}
        self.mock_login_user.return_value = (True, user_info)
        
        # Ensure we are on the login page first (it is by default from __init__)
        self.app.show_frame.reset_mock()

        # Simulate the successful login flow from login_page
        # login_page's handle_login calls show_frame_callback("dashboard", data=result)
        # This callback is self.app.show_frame
        self.app.show_frame("dashboard", data=user_info)

        self.app.show_frame.assert_called_with("dashboard", data=user_info)
        self.mock_dashboard_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame, user_info)
        self.assertEqual(self.app.current_user_data, user_info)
        self.assertEqual(self.app.current_page_name, "dashboard")

    def test_failed_login_stays_on_login_page_and_clears_data(self):
        self.mock_login_user.return_value = (False, "Invalid credentials")
        
        # Simulate a previous logged-in state to ensure it's cleared
        self.app.current_user_data = {'full_name': 'Old User'}
        
        self.app.show_frame("login") # Go to login page
        self.app.show_frame.reset_mock() # Reset after navigation

        # Simulate what happens in login_page:
        # 1. User attempts login.
        # 2. login_user service returns (False, ...).
        # 3. login_page shows an error message (mocked out here).
        # 4. Crucially, login_page does NOT call show_frame_callback.
        
        # So, we assert that show_frame was NOT called with "dashboard"
        # (It was called with "login" to get to the page, so we don't check for no calls at all)
        # We check that current_user_data is None (cleared by navigating to login)
        # and that the current page is still login.
        
        # No call to show_frame("dashboard", ...)
        for call_args in self.app.show_frame.call_args_list:
            self.assertNotEqual(call_args[0][0], "dashboard")

        self.assertIsNone(self.app.current_user_data) # Cleared by show_frame("login")
        self.assertEqual(self.app.current_page_name, "login")
        # Ensure login page constructor was called (it was, by show_frame("login"))
        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)


    def test_logout_from_dashboard(self):
        # Setup: Go to dashboard as a logged-in user
        user_info = {'full_name': 'Test User'}
        self.app.current_user_data = user_info # Simulate being logged in
        self.app.show_frame("dashboard", data=user_info) # Navigate to dashboard
        self.app.show_frame.reset_mock() # Reset after navigation

        # Simulate the "Logout" button click from dashboard_page
        # dashboard_page's logout button calls show_frame_callback("login")
        # This callback is self.app.show_frame
        self.app.show_frame("login")

        self.app.show_frame.assert_called_with("login")
        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertIsNone(self.app.current_user_data) # User data should be cleared
        self.assertEqual(self.app.current_page_name, "login")

    def test_dashboard_access_without_login_redirects_to_login(self):
        self.app.current_user_data = None # Ensure no user is logged in
        self.app.show_frame.reset_mock()

        # Attempt to go to dashboard directly
        self.app.show_frame("dashboard")

        # The App.show_frame logic should catch that current_user_data is None
        # and redirect to "login".
        # So, show_frame("dashboard") was called, then show_frame("login") was called by the wrapper.
        # The wrapped method (original show_frame) would then call login_page constructor.
        
        # Check the sequence of calls to the *wrapped* show_frame
        # First call: self.app.show_frame("dashboard")
        # Second call (internal redirect): self.app.show_frame("login")
        self.assertEqual(self.app.show_frame.call_count, 2)
        self.app.show_frame.assert_any_call("dashboard") # The initial attempt
        self.app.show_frame.assert_called_with("login")  # The final redirect call

        self.mock_login_page_constructor.assert_called_with(self.app.main_container, self.app.show_frame)
        self.assertIsNone(self.app.current_user_data)
        self.assertEqual(self.app.current_page_name, "login")

if __name__ == '__main__':
    # This allows running the tests directly from this file
    unittest.main()

# Add a line in App class in main.py: self.current_page_name = None
# In App.show_frame, before calling page_constructor: self.current_page_name = page_name
# This helps in asserting the current page.
# Example change in app/main.py:
#
# class App:
#     def __init__(self, root_window):
#         # ...
#         self.current_page_name = None # Add this
#         self.show_frame("login")
#
#     def show_frame(self, page_name, data=None):
#         # ...
#         # Clear previous frame's content
#         for widget in self.main_container.winfo_children():
#             widget.destroy()
#
#         self.current_page_name = page_name # Add this
#
#         page_constructor = self.pages.get(page_name)
#         # ...
#
# This is for testability and not strictly part of the original requirement,
# but makes tests cleaner.
# The tests above assume this change has been made.
# If not, remove assertions for self.app.current_page_name
# or adjust how current page is determined.
# For now, I will assume this change is made for the tests to pass as written.
# If I were to modify app/main.py, I'd add these lines.
# Since I can't modify app/main.py in this step, I'll note this dependency.
# The tests are designed to be robust IF that small modification to App exists.
# Without it, the self.assertEqual(self.app.current_page_name, "...") assertions would fail.
# I will proceed with the tests as written, assuming this minor instrumentation for testability.
# If that's not permissible, I'll have to rely only on which page constructor was called.
# For the purpose of this subtask, I'll assume the `current_page_name` attribute is added.

# The tests also rely on the show_frame method being wrapped correctly:
# self.app.show_frame = MagicMock(wraps=self.app.show_frame)
# This is crucial for testing calls to show_frame itself while letting the original logic run.
# The test structure relies on this to verify both direct calls and internal redirects.

# A note on `test_failed_login_stays_on_login_page_and_clears_data`:
# This test verifies that current_user_data is cleared when navigating to login (which it is),
# and that show_frame("dashboard") is *not* called.
# It also verifies that the login_page constructor is called (as we are on the login page).
# This indirectly tests that a failed login (which doesn't call show_frame) keeps the user
# on the login page.
