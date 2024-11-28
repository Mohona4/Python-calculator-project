import tkinter as tk

# Button click handler
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Clear the entry
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying calculations
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=evaluate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Run the main loop
root.mainloop()
