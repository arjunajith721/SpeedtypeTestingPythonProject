import tkinter as tk
import time
from tkinter import messagebox
import subprocess

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")
        self.root.geometry("800x400")

        # Load test settings
        self.load_settings()

        # Instructions
        instruction_label = tk.Label(root, text="Press 'Get Started' to begin typing. Press 'Enter' to end the test early.", font=("Helvetica", 14))
        instruction_label.pack(pady=10)

        # Display the text to type
        self.text_to_type_label = tk.Label(root, text=self.custom_text, font=("Helvetica", 12), wraplength=700)
        self.text_to_type_label.pack(pady=20)

        # Typing input box
        self.input_text = tk.Text(root, height=5, width=60, font=("Helvetica", 12))
        self.input_text.pack(pady=10)
        self.input_text.config(state="disabled")  # Disable until the test starts
        self.input_text.bind("<KeyRelease>", self.check_typing)
        self.input_text.bind("<Return>", self.stop_test)  # Bind Enter key to stop the test

        # Timer
        self.time_remaining = int(self.time_limit.strip("s"))
        self.timer_label = tk.Label(root, text=f"Time remaining: {self.time_remaining}s", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        # Get Started button
        start_button = tk.Button(root, text="Get Started", command=self.start_test, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        start_button.pack(pady=10)

        # Back button
        back_button = tk.Button(root, text="Back", command=self.go_back, font=("Helvetica", 12), bg="#f44336", fg="white")
        back_button.pack(pady=20)

        # Stats
        self.words_typed = 0
        self.errors = 0

    def load_settings(self):
        """Load typing test settings from the file."""
        try:
            with open("settings.txt", "r") as file:
                settings = file.readlines()
                self.time_limit = settings[0].strip()
                self.difficulty = settings[1].strip()
                self.tricky_typing = settings[2].strip()
                self.custom_text = settings[3].strip() if len(settings) > 3 else "The quick brown fox jumps over the lazy dog."
        except FileNotFoundError:
            messagebox.showerror("Error", "Settings file not found. Please configure the test from the start page.")
            self.root.destroy()

    def start_test(self):
        """Enable typing input and start the timer."""
        self.input_text.config(state="normal")  # Enable typing
        self.input_text.focus_set()  # Set focus to the typing area
        self.start_timer()

    def start_timer(self):
        """Start the countdown timer."""
        self.update_timer()

    def update_timer(self):
        """Update the timer every second."""
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time remaining: {self.time_remaining}s")
            self.root.after(1000, self.update_timer)
        else:
            self.finish_test()

    def check_typing(self, event):
        """Check the typing progress and calculate accuracy."""
        typed_text = self.input_text.get("1.0", "end-1c")
        correct_text = self.custom_text[:len(typed_text)]

        self.words_typed = len(typed_text.split())
        self.errors = sum(1 for i, c in enumerate(typed_text) if i < len(correct_text) and c != correct_text[i])

    def stop_test(self, event=None):
        """Stop the test early by pressing Enter."""
        self.time_remaining = 0  # Set time to zero to trigger finish
        self.finish_test()

    def finish_test(self):
        """Finish the test and show the results."""
        wpm = self.words_typed / (int(self.time_limit.strip("s")) / 60)
        accuracy = max(0, (1 - self.errors / max(1, len(self.custom_text))) * 100)

        messagebox.showinfo("Test Results", f"Words per minute: {wpm:.2f}\nAccuracy: {accuracy:.2f}%")
        self.root.destroy()

    def go_back(self):
        """Go back to the Get Started screen."""
        self.root.destroy()
        subprocess.Popen(["python", "get_started.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
