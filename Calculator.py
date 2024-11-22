import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')


def calculate_persent():
    try:
        value = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')


def calculate_square():
    try:
        value = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')        


master = tk.Tk()
master.title('Calculator')

entry = tk.Entry(master, width=30, borderwidth=5, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0),('5', 2, 1),('6', 2, 2),('*', 2, 3),
    ('1', 3, 0),('2', 3, 1),('3', 3, 2),('-', 3, 3),
    ('C', 4, 0),('0', 4, 1),('=', 4, 2),('+', 4, 3),
    ('%', 5, 0),('x^2', 5, 1),
]

for (text, row, col) in buttons:
    if text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    elif text == '%':
        action = calculate_persent
    elif text == 'x^2':
        action = calculate_square
    else:
        action = lambda x=text: button_click(x) 

    tk.Button(
        master, text=text, padx=20, pady=20, font=('Arial', 14), command=action
    ).grid(row=row, column=col)

master.mainloop()