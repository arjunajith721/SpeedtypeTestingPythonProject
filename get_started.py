import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import leaderboard  # Import the leaderboard functionality
import random

class GetStartedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get Started")
        self.root.geometry("900x600")

        # Label for Title
        title_label = tk.Label(root, text="Typing Test Setup", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=20)

        # Dropdown for Time Selection
        tk.Label(root, text="Select Time:", font=("Helvetica", 12)).pack(pady=5)
        self.time_var = tk.StringVar(value="60s")
        time_options = ["30s", "60s", "120s", "180s"]
        self.time_dropdown = ttk.Combobox(root, textvariable=self.time_var, values=time_options, state="readonly")
        self.time_dropdown.pack(pady=5)

        # Dropdown for Difficulty Level
        tk.Label(root, text="Select Difficulty:", font=("Helvetica", 12)).pack(pady=5)
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulty_options = ["Easy", "Medium", "Hard"]
        self.difficulty_dropdown = ttk.Combobox(root, textvariable=self.difficulty_var, values=difficulty_options, state="readonly")
        self.difficulty_dropdown.pack(pady=5)

        # Dropdown for Tricky Typing
        tk.Label(root, text="Select Tricky Typing:", font=("Helvetica", 12)).pack(pady=5)
        self.tricky_typing_var = tk.StringVar(value="Off")
        tricky_typing_options = ["Off", "On"]
        self.tricky_typing_dropdown = ttk.Combobox(root, textvariable=self.tricky_typing_var, values=tricky_typing_options, state="readonly")
        self.tricky_typing_dropdown.pack(pady=5)

        # Textbox for Custom Text
        tk.Label(root, text="Enter Custom Text (optional):", font=("Helvetica", 12)).pack(pady=5)
        self.custom_text = tk.Text(root, height=5, width=40)
        self.custom_text.pack(pady=5)

        # Start Button
        start_button = tk.Button(root, text="Get Started", command=self.start_typing_test, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        start_button.pack(pady=20)

        # Leaderboard Box (Yellow)
        leaderboard_frame = tk.Frame(root, bg="yellow", bd=2, relief="solid")
        leaderboard_frame.pack(pady=10, fill="y")

        leaderboard_label = tk.Label(leaderboard_frame, text="Show Leaderboard", font=("Helvetica", 12, "bold"), bg="yellow")
        leaderboard_label.pack(pady=5)

        leaderboard_button = tk.Button(leaderboard_frame, text="View Leaderboard", command=self.show_leaderboard, font=("Helvetica", 12), bg="#FFC107", fg="white")
        leaderboard_button.pack(pady=5)

    def start_typing_test(self):
        # Gather selected options
        time_limit = self.time_var.get()
        difficulty = self.difficulty_var.get()
        tricky_typing = self.tricky_typing_var.get()
        custom_text = self.custom_text.get("1.0", "end-1c").strip()

        # Default texts for the typing test
        default_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Typing tests are an excellent way to improve your speed and accuracy.",
            "Python is a powerful programming language used in many applications.",
            "A journey of a thousand miles begins with a single step.",
            "Consistency is the key to mastering any skill.",
            "In a world where you can be anything, be kind.",
            "Learning to code opens up many exciting career opportunities.",
            "Never stop learning, because life never stops teaching."
        ]

        # If no custom text is provided, select a random default text
        if not custom_text:
            custom_text = random.choice(default_texts)

        # Save selected settings to pass to typing_test.py
        with open("settings.txt", "w") as file:
            file.write(f"{time_limit}\n{difficulty}\n{tricky_typing}\n{custom_text}")

        # Open typing_test.py
        subprocess.Popen(["python", "typing_test.py"])

        # Close this window
        self.root.destroy()

    def show_leaderboard(self):
        # Open the leaderboard window
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_app = leaderboard.LeaderboardApp(leaderboard_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = GetStartedApp(root)
    root.mainloop()
