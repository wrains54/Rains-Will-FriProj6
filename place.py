import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

username_label = ttk.Label(root, text="Username:")
username_label.place(x=50, y=50, width=100, height=25)

username_entry = ttk.Entry(root)
username_entry.place(x=150, y=50, width=100, height=25)

password_label = ttk.Label(root, text="Password:")
password_label.place(x=50, y=80, width=100, height=25)

password_entry = ttk.Entry(root, show="*")
password_entry.place(x=150, y=80, width=100, height=25)

login_button = ttk.Button(root, text="Login")
login_button.place(x=150, y=110, width=100, height=25)

root.mainloop()