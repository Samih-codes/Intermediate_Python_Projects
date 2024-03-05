from tkinter import *
import pandas
from random import choice
# ---------------------------- FlashCard Generator ------------------------------- #
current_card = {}
word_list = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/arabic_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient='records')


# Function to update the flashcard with a new word
def next_flashcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_list)
    canvas.itemconfig(title_text, text = "Arabic", fill = "black")
    canvas.itemconfig(word_text, text=current_card["Arabic"],fill = "black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)

# Function to flip the card

def flip_card():
    canvas.itemconfig(title_text, fill = "white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

# Function to handle when user knows the word
def is_known():
    word_list.remove(current_card)
    new_data = pandas.DataFrame(word_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_flashcard()
# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Quranic Arabic Flashcards")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 293, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan= 2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column = 1, row = 1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, fg= BACKGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_flashcard)
wrong_button.grid(column = 0, row = 1)


next_flashcard()

window.mainloop()

