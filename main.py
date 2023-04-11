from tkinter import *
import pandas
import random
word = None
word_2 = None
BACKGROUND_COLOR = "#B1DDC6"
ls = []
ls_x = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


def generate_word():
    global timer, data, word
    canvas.itemconfig(canvas_img, image=front_img)
    try:
        word = random.choice(data["French"])
    except IndexError:
        data = pandas.read_csv("data/french_words.csv")
        data.to_csv('data/words_to_learn.csv', index=False, header=True)
        word = random.choice(data["French"])
    canvas.itemconfig(text_2, text=word, fill="black")
    canvas.itemconfig(text_1, text="French", fill="black")
    timer = window.after(3000, next_card)


def next_card():
    window.after_cancel(timer)
    word_2 = data[data.French == word]
    ls = word_2.values.tolist()
    canvas.itemconfig(canvas_img, image=bach_img)
    canvas.itemconfig(text_1, text="English", fill="white")
    canvas.itemconfig(text_2, text=ls[0][1], fill="white")


def known_word():
    global data, word_2
    window.after_cancel(timer)
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
    x = data[data.French == word].index
    ls_x = x.tolist()
    data = data.drop(ls_x[0])
    data = pandas.DataFrame(data)
    data.to_csv('data/words_to_learn.csv', index=False, header=True)
    data = pandas.read_csv("data/words_to_learn.csv")
    word_2 = data[data.French == word]
    generate_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="C:/Users/Dado/PycharmProject/1/12/Day_31_Flash_Card_App/images/card_front.png")
bach_img = PhotoImage(file="C:/Users/Dado/PycharmProject/1/12/Day_31_Flash_Card_App/images/card_back.png")
canvas_img = canvas.create_image(400, 270, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)


text_1 = canvas.create_text(400, 200, text="", fill="black", font=("arial", 30, "bold"))
text_2 = canvas.create_text(400, 350, text="", fill="black", font=("arial", 45, "bold"))

right_img = PhotoImage(file="C:/Users/Dado/PycharmProject/1/12/Day_31_Flash_Card_App/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="C:/Users/Dado/PycharmProject/1/12/Day_31_Flash_Card_App/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

generate_word()
window.mainloop()
