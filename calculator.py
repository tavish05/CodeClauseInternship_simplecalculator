import tkinter as tk

def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text=f"Result: {result}")

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text=f"Result: {result}")

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text=f"Result: {result}")

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        label_result.config(text="Error: Division by zero")
    else:
        result = num1 / num2
        label_result.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input fields
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(window)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Create operation buttons
button_add = tk.Button(window, text="+", command=add)
button_add.grid(row=1, column=0, padx=10, pady=10)

button_subtract = tk.Button(window, text="-", command=subtract)
button_subtract.grid(row=1, column=1, padx=10, pady=10)

button_multiply = tk.Button(window, text="*", command=multiply)
button_multiply.grid(row=2, column=0, padx=10, pady=10)

button_divide = tk.Button(window, text="/", command=divide)
button_divide.grid(row=2, column=1, padx=10, pady=10)

# Create result label
label_result = tk.Label(window, text="Result:")
label_result.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main loop
window.mainloop()
