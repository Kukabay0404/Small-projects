import tkinter as tk
import random
from tkinter import messagebox

random_number = random.randint(0, 101)
def guess_number():
    global random_number
    try:
        user_input = int(entry.get())
        if user_input > random_number:
            result_label.config(text='Number is lower', fg='red') 
        elif user_input < random_number:
            result_label.config(text='Number is higher', fg='red') 
        else:
            result_label.config(text='You right', fg='green') 
            messagebox.showinfo('Congratulations', 'You win')
            reset_game()
    except ValueError:
        result_label.config(text='Error', fg='green') 
            

def reset_game():
    global random_number
    random_number = random.randint(0, 101)
    entry.delete(0, tk.END)
    result_label.config(text='')


master = tk.Tk()
master.title('Guess number')
master.geometry('300x200')

entry = tk.Entry(master, width=20)
entry.pack(pady=10)

button = tk.Button(master, text='Guess', command=guess_number)
button.pack(pady=5)

result_label = tk.Label(master, text='')
result_label.pack(pady=10)

master.mainloop()