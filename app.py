import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Weak Password", "Password length should be at least 6 characters.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# Main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#1e1e2e")

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), fg="#ff79c6", bg="#1e1e2e")
title_label.pack(pady=10)

# Length input frame
frame_length = tk.Frame(root, bg="#1e1e2e")
frame_length.pack(pady=10)

length_label = tk.Label(frame_length, text="Password Length:", font=("Arial", 12), fg="#8be9fd", bg="#1e1e2e")
length_label.grid(row=0, column=0, padx=10)

entry_length = tk.Entry(frame_length, font=("Arial", 12), width=5, justify="center")
entry_length.grid(row=0, column=1)

# Generate button
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#50fa7b", fg="#1e1e2e", command=generate_password)
btn_generate.pack(pady=10)

# Password entry
entry_password = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
entry_password.pack(pady=10)

# Copy button
btn_copy = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#bd93f9", fg="#1e1e2e", command=copy_to_clipboard)
btn_copy.pack(pady=10)

# Run the application
root.mainloop()
