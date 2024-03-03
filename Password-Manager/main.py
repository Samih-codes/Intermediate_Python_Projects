from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Function to generate a random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Function to save the password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty!")
    else:
        messagebox.askokcancel(title=website, message=f"You entered the following details: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")  # White background color

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")  # White background color
website_label.grid(column=0, row=1, sticky="E")
email_label = Label(text="Email/Username:", bg="white")  # White background color
email_label.grid(column=0, row=2, sticky="E")
password_label = Label(text="Password:", bg="white")  # White background color
password_label.grid(column=0, row=3, sticky="E")

# Entry Bars
website_entry = Entry(width=35, bg="white")  # Light pink background color
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35, bg="white")  # Light pink background color
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "samih@gmail.com")
password_entry = Entry(width=21, bg="white")  # Light pink background color
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg="gold")  # Light pink background color
generate_password_button.grid(column=2, row=3, sticky="EW")
save_button = Button(text="Save Password", width=36, command=save, bg="#90EE90")  # Sky blue background color
save_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
