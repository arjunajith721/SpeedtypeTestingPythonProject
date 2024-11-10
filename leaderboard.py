import sqlite3
import tkinter as tk
from tkinter import messagebox
import subprocess  # Import subprocess to run get_started.py
from PIL import Image, ImageTk

# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect("leaderboard.db")
    return conn

# Create leaderboard table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        accuracy REAL,
                        words_typed INTEGER,
                        time_taken INTEGER
                    )''')
    conn.commit()
    conn.close()

# Insert a new result into the leaderboard
def insert_result(name, accuracy, words_typed, time_taken):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (name, accuracy, words_typed, time_taken) VALUES (?, ?, ?, ?)",
                   (name, accuracy, words_typed, time_taken))
    conn.commit()
    conn.close()

# Get top 5 leaderboard results ordered by accuracy
def get_leaderboard():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, accuracy, words_typed, time_taken FROM leaderboard ORDER BY accuracy DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    return rows

class LeaderboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leaderboard")
        self.root.geometry("600x400")

        # Create a Canvas to hold the background image
        canvas = tk.Canvas(root, width=600, height=400)
        canvas.pack(fill="both", expand=True)

        # Try to load and set a background image
        try:
            image = Image.open("bg2.jpg")  # Update the path to your image
            image = image.resize((600, 400), Image.ANTIALIAS)  # Resize to fit the window
            background_image = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, image=background_image, anchor="nw")
            # Keep a reference to the image to prevent garbage collection
            canvas.image = background_image
        except Exception as e:
            print(f"Error loading background image: {e}")

        # Create a frame to contain all content (Gray9 background color)
        content_frame = tk.Frame(root, bg="#1C1C1C", bd=2)  # Set gray9 color here
        content_frame.place(relwidth=1, relheight=1)  # Make it fill the window

        # Create the table if it doesn't exist
        create_table()

        # Title
        title_label = tk.Label(content_frame, text="Typing Test Leaderboard", font=("Helvetica", 18, "bold"), bg="#1C1C1C", fg="white")
        title_label.pack(pady=20)

        # Display leaderboard
        self.leaderboard_listbox = tk.Listbox(content_frame, width=50, height=10, font=("Helvetica", 12), bg="#333333", fg="white")
        self.leaderboard_listbox.pack(pady=10)

        # Load leaderboard results
        self.load_leaderboard()

        # Back to Test Button
        back_button = tk.Button(content_frame, text="Back to Get Started", command=self.back_to_test, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        back_button.pack(pady=20)

    def load_leaderboard(self):
        # Clear previous leaderboard
        self.leaderboard_listbox.delete(0, tk.END)

        # Fetch leaderboard results
        leaderboard = get_leaderboard()

        # Insert leaderboard results into Listbox
        for index, (name, accuracy, words_typed, time_taken) in enumerate(leaderboard):
            self.leaderboard_listbox.insert(tk.END, f"{index + 1}. {name} - Accuracy: {accuracy:.2f}% - Words: {words_typed} - Time: {time_taken}s")

    def back_to_test(self):
        self.root.destroy()  # Close leaderboard window

        # Open the GetStartedApp window
        subprocess.Popen(["python", "get_started.py"])


if __name__ == "__main__":
    root = tk.Tk()
    app = LeaderboardApp(root)
    root.mainloop()
