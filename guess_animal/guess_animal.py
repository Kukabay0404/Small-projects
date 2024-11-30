import tkinter as tk
from PIL import Image, ImageTk
import os

questions = [
    "1. Млекопитающее или Рыба? (a, b)",
    "2. Хищное, Грызун или Травоядное? (a, b, c)",
    "3. Крупный или Мелкий? (a, b)",
    "4. Рычит, Пищит или Трубит? (a, b, c)"
]

current_question = 0
user_answers = []

animals = {
    ('a', 'a', 'a', 'a'): "tiger.jpg",
    ('a', 'b', 'b', 'a'): "mouse.jpg",
    ('a', 'c', 'a', 'c'): "elephant.jpg"
}


def next_question():
    global current_question
    answer = entry.get().strip().lower()
    if not answer:
        question.config(text="Введите ответ!")
        return

    user_answers.append(answer)
    entry.delete(0, tk.END)

    if current_question + 1 < len(questions):
        current_question += 1
        question.config(text=questions[current_question])
    else:
        question.config(text="Игра завершена!")
        entry.config(state="disabled")
        button_next.config(state="disabled")
        show_result_image()


def show_result_image():
    global image_label, image
    img_path = animals.get(tuple(user_answers))
    if not img_path:
        question.config(text="Ответы не совпадают с животными!")
        return

    try:
        img_path = os.path.join(os.path.dirname(__file__), img_path)
        original_image = Image.open(img_path).resize((300, 300))
        image = ImageTk.PhotoImage(original_image)
        image_label.config(image=image)
        image_label.image = image
    except Exception as e:
        question.config(text=f"Ошибка загрузки изображения: {e}")
        return

    reset_button.pack(pady=10)


def reset_game():
    global current_question, user_answers
    current_question = 0
    user_answers = []
    question.config(text=questions[current_question])
    entry.config(state="normal")
    button_next.config(state="normal")
    entry.delete(0, tk.END)
    image_label.config(image="")
    reset_button.pack_forget()


master = tk.Tk()
master.title("Угадай животное")
master.geometry("400x500")

intro_label = tk.Label(master, text="Ответьте на вопросы, чтобы угадать животное!\nВыберите a, b или c.",
                       font=("Arial", 12), wraplength=380)
intro_label.pack(pady=10)

question = tk.Label(master, text=questions[current_question], font=("Arial", 14), wraplength=380)
question.pack(pady=20)

entry = tk.Entry(master, width=30, font=("Arial", 12))
entry.pack(pady=10)

button_next = tk.Button(master, text="Ответить", command=next_question, font=("Arial", 12))
button_next.pack(pady=10)

image_label = tk.Label(master)
image_label.pack(pady=20)

reset_button = tk.Button(master, text="Сыграть ещё раз", command=reset_game, font=("Arial", 12))
reset_button.pack_forget()

master.mainloop()
