from tkinter import *

def button_clicked():
    miles = float(input.get())  # Retrieve the value from the Entry widget and convert to float
    kilometers = miles * 1.60934  # Convert miles to kilometers
    answer.config(text=f"{kilometers:.2f}")


window = Tk()
window.title("Miles To Kilometers Converter")
window.minsize(width=350, height=125)
window.config(padx=20, pady=20)

# Labels
equal_to = Label(text="is equal to", font= "Anta")
equal_to.grid(column=0, row=1)
equal_to.config(padx=10, pady=10)

miles_label = Label(text= "Miles", font= "Anta")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

Km = Label(text="Km", font= "Anta")
Km.grid(column=2, row=1)
Km.config(padx=10, pady=10)

answer = Label(text="", font= "Anta")
answer.grid(column=1, row=1)
answer.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# Mile Entry
input = Entry(width=9)
input.grid(column=1, row=0)

window.mainloop()
