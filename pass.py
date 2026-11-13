
import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    status.config(text="Password Copied!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#1e1e2e")

tk.Label(root, text="🔐 Password Generator",
         font=("Arial", 20, "bold"),
         bg="#1e1e2e", fg="white").pack(pady=20)

tk.Label(root, text="Enter Password Length:",
         bg="#1e1e2e", fg="white").pack()

length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=8)

password_entry = tk.Entry(root, width=35,
                          justify="center", font=("Arial", 11))
password_entry.pack(pady=15)

tk.Button(root, text="Generate Password",
          command=generate_password,
          bg="#7c3aed", fg="white",
          font=("Arial", 11, "bold")).pack(pady=5)

tk.Button(root, text="Copy Password",
          command=copy_password,
          bg="#16a34a", fg="white").pack(pady=5)

status = tk.Label(root, text="", bg="#1e1e2e", fg="#22c55e")
status.pack(pady=10)

root.mainloop()
