from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Anta", 16, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		# self.high_score = 0
		with open("data.txt") as data:
			self.high_score= int(data.read())
		self.color("yellow")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()  # Hide the turtle icon
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} Highscore: {self.high_score}", align= ALIGNMENT, font= FONT)

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", mode="w") as data:
				data.write(f"{self.high_score}")
		self.score = 0
		self.update_scoreboard()

	# Old Code:
	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.color("white")
	# 	self.write("GAME OVER", align= ALIGNMENT, font = ("Anta", 20, "normal"))
