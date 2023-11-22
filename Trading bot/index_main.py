import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_name = entry.get()
    messagebox.showinfo("Greetings", f"Hello, {user_name}!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI App")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button
button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()
