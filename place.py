import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

username_label = ttk.Label(root, text="Username:")
username_label.place(x=50, y=50, width=100, height=25)

username_entry = ttk.Entry(root)
username_entry.place(x=150, y=50, width=100, height=25)