import tkinter as tk


# Function to evaluate the equation
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)


# Function to add a character to the entry field
def add_character(char):
    entry.insert(tk.END, char)


# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")

# Create the entry field
entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = tk.Button(root, text="1", width=5, height=2,
                     command=lambda: add_character('1'))
button_1.grid(row=1, column=0, padx=5, pady=5)

button_2 = tk.Button(root, text="2", width=5, height=2,
                     command=lambda: add_character('2'))
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = tk.Button(root, text="3", width=5, height=2,
                     command=lambda: add_character('3'))
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = tk.Button(root, text="4", width=5, height=2,
                     command=lambda: add_character('4'))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(root, text="5", width=5, height=2,
                     command=lambda: add_character('5'))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(root, text="6", width=5, height=2,
                     command=lambda: add_character('6'))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_7 = tk.Button(root, text="7", width=5, height=2,
                     command=lambda: add_character('7'))
button_7.grid(row=3, column=0, padx=5, pady=5)

button_8 = tk.Button(root, text="8", width=5, height=2,
                     command=lambda: add_character('8'))
button_8.grid(row=3, column=1, padx=5, pady=5)

button_9 = tk.Button(root, text="9", width=5, height=2,
                     command=lambda: add_character('9'))
button_9.grid(row=3, column=2, padx=5, pady=5)

# Create the number buttons
button_0 = tk.Button(root, text="0", width=5, height=2,
                     command=lambda: add_character('0'))
button_0.grid(row=4, column=0, padx=5, pady=5)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, width=5, height=2,
                       command=lambda operator=operator: add_character(operator))
    button.grid(row=i + 1, column=3, padx=5, pady=5)

# Create the additional buttons
button_clear = tk.Button(root, text="C", width=5, height=2, command=clear)
button_clear.grid(row=1, column=4, padx=5, pady=5)

button_decimal = tk.Button(root, text=".", width=5, height=2,
                           command=lambda: add_character('.'))
button_decimal.grid(row=4, column=1, padx=5, pady=5)

button_equals = tk.Button(root, text="=", width=5, height=5, command=evaluate)
button_equals.grid(row=4, column=2, rowspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
