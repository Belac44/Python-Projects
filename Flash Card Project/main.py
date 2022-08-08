from tkinter import *
from random import *
import pandas as pd
import time

current_card=0

df = pd.read_csv("data/french_words.csv")


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    num = randint(0, 100)
    current_card = num
    print(num)
    word = df.iloc[num]
    canvas.itemconfig(canvas_text, text=word.French, fill="black")
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    new_flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(canvas_text, text=df.iloc[current_card].English, fill="White")
    canvas.itemconfig(canvas_title, text="English", fill="white")


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
canvas_title = canvas.create_text(400, 100, text="", font=("Arial", 40, "italic"))
canvas_text = canvas.create_text(400, 260, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cancel_image = PhotoImage(file="images/wrong.png")
cancel = Button(image=cancel_image, highlightthickness=0, command=generate_word)
cancel.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=generate_word)
right.grid(column=1, row=1)


window.mainloop()

