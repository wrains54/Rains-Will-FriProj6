import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, state='disabled', width=40)
entry.pack(padx=10, pady=10)

# Frame for organizing the buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Buttons
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0', '+', '-', 'x', '/',
    '='
]

# Creating and packing buttons in the frame using a loop
for button in buttons:
    b = tk.Button(button_frame, text=button, width=5, height=2)
    b.pack(side='left', padx=2, pady=2)

root.mainloop()