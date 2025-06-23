import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm
import time
import threading

def show_progress():
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress")
    progress_label = tk.Label(progress_window, text="Processing...")
    progress_label.pack(pady=10)
    progress_bar = tk.Label(progress_window, text="", anchor="w", bg="blue", width=50)
    progress_bar.pack(pady=10)

    for i in tqdm(range(100)):
        time.sleep(0.1)
        progress_bar.config(width=i)
        progress_window.update_idletasks()

    progress_window.destroy()
    messagebox.showinfo(f" See outside")

def on_submit():
    threading.Thread(target=show_progress).start()

# Create the main window
root = tk.Tk()
root.title("City Name Entry")

# Create a label
label = tk.Label(root, text="Enter city name:")
label.pack(pady=10)

# Create a text entry field
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
