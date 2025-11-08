import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

display = tk.Entry(root, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, pady=10)

current_text = ""

def button_click(number):
    global current_text
    current_text = current_text + str(number)
    display.delete(0, tk.END)
    display.insert(0, current_text)

def clear():
    global current_text
    current_text = ""
    display.delete(0, tk.END)

def equals():
    global current_text
    try:
        result = str(eval(current_text))
        display.delete(0, tk.END)
        display.insert(0, result)
        current_text = result
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        current_text = ""

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=equals).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=row_val, column=col_val)

root.mainloop()