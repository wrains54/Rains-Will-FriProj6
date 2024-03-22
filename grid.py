import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign Up")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


name_label = ttk.Label(root, text="Name:")
name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)


email_label = ttk.Label(root, text="Email:")
email_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

email_entry = ttk.Entry(root)
email_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)


password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

sign_up_button = ttk.Button(root, text="Sign Up Now")
sign_up_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()