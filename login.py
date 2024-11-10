import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ensure Pillow is installed
import subprocess
import sys
import os

# Predefined credentials (for simplicity, you can save and load this later)
USERNAMES = {"1": "1"}  # username: password dictionary for existing users

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the credentials match the predefined ones
    if username == "1" and password == "1":
        messagebox.showinfo("Login Status", "Login Successful!")
        root.destroy()  # Close the login window

        # Get the path of the current script and join it with get_started.py
        script_dir = os.path.dirname(os.path.abspath(__file__))
        started_path = os.path.join(script_dir, "get_started.py")

        # Open get_started.py
        subprocess.Popen([sys.executable, started_path])
    else:
        messagebox.showerror("Login Status", "Invalid username or password.")

def add_user():
    # Create a new window for adding a user
    add_user_window = tk.Toplevel(root)
    add_user_window.title("Add New User")
    add_user_window.geometry("400x300")

    # Set the background color of the add_user_window to black
    add_user_window.config(bg="black")

    # New Username label and entry
    new_username_label = tk.Label(add_user_window, text="New Username", font=("Helvetica", 12), bg="black", fg="white")
    new_username_label.pack(pady=5)
    new_username_entry = tk.Entry(add_user_window, font=("Helvetica", 12))
    new_username_entry.pack(pady=5)

    # New Password label and entry
    new_password_label = tk.Label(add_user_window, text="New Password", font=("Helvetica", 12), bg="black", fg="white")
    new_password_label.pack(pady=5)
    new_password_entry = tk.Entry(add_user_window, show="*", font=("Helvetica", 12))
    new_password_entry.pack(pady=5)

    def save_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        if new_username and new_password:
            # Save the new user credentials
            USERNAMES[new_username] = new_password
            messagebox.showinfo("User Added", "New user added successfully!")
            add_user_window.destroy()  # Close the "Add New User" window
        else:
            messagebox.showerror("Error", "Both fields are required.")

    # OK Button to save the new user
    ok_button = tk.Button(add_user_window, text="OK", font=("Helvetica", 12), command=save_user, bg="black", fg="white")
    ok_button.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("900x600")

# Set the background color of the login window to black
root.config(bg="black")

# Load background image (optional, since you're using a black background)
try:
    image = Image.open("bg2.jpg")
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Set image to cover entire window
except Exception as e:
    print(f"Error loading background image: {e}")

# Center Frame for the Login Form
frame = tk.Frame(root, bg="black", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.5)

# Title Label
title_label = tk.Label(frame, text="Login", font=("Helvetica", 18, "bold"), bg="black", fg="white")
title_label.pack(pady=10)

# Username label and entry
username_label = tk.Label(frame, text="Username", font=("Helvetica", 12), bg="black", fg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(frame, font=("Helvetica", 12))
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(frame, text="Password", font=("Helvetica", 12), bg="black", fg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(frame, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(frame, text="Login", font=("Helvetica", 12), command=login, bg="black", fg="white")
login_button.pack(pady=20)

# Add New User button
add_user_button = tk.Button(frame, text="Add New User", font=("Helvetica", 12), command=add_user, bg="black", fg="white")
add_user_button.pack(pady=5)

# Run the main event loop
root.mainloop()
