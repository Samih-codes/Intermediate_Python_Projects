from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Anta", 16, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("yellow")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()  # Hide the turtle icon
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.color("white")
		self.write("GAME OVER", align= ALIGNMENT, font = ("Anta", 20, "normal"))