from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Anta", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-240, 260)
        self.hideturtle()  # Hide the turtle icon
        self.update_level_score()

    def update_level_score(self):
        self.write(f"Level: {self.level}", align= ALIGNMENT, font= FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=("Anta", 20, "normal"))
