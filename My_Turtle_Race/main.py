from turtle import Turtle, Screen
import random

# The Setup
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your prediction", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# Creating turtles for the race
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Race
is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                winner_message = f"You've won! The {winning_color} turtle is the winner!"
            else:
                winner_message = f"You've lost! The {winning_color} turtle is the winner!"
            print(winner_message)
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Clear screen
screen.clear()

# Display winner message at center of the screen
winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, 0)
winner_turtle.write(winner_message, align="center", font=("Arial", 15, "italic"))

screen.exitonclick()
