# name = input(' name (can be fake one) ')
# age = int(input(' age " if you want to put.'))
# intrest = input(' type your intrests : example : taylor swift ')
# pn = int(input('area code. (the first number in bracket on your phone number)'))
# rpn = int(input(' rest of phone number'))




import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
app = tk.Tk()
app.title("Calculator App")
# 
# Entry widget for user input
entry = tk.Entry(app, width=20)
entry.grid(row=0, column=0, columnspan=4)

# # Result label
result_label = tk.Label(app, text="Result: ")
result_label.grid(row=1, column=0, columnspan=4)

# # Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 2
col_val = 0

for button in buttons:
    tk.Button(app, text=button, width=5, command=lambda b=button: entry.insert(tk.END, b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()


