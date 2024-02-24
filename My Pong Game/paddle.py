from turtle import Turtle
MOVE_DISTANCE = 40
class Paddle(Turtle):

	def __init__(self,position, color=None):
		super().__init__()
		self.shape("square")
		self.shapesize(stretch_wid=5, stretch_len=1)
		if position[0] > 0:
			self.color("blue")
		else:
			self.color("red")
		self.penup()
		self.goto(position)

	def paddle_up(self):
		new_y = self.ycor() + MOVE_DISTANCE
		if new_y < 280:  # Check if the new y-coordinate is within bounds
			self.goto(self.xcor(), new_y)

	def paddle_down(self):
		new_y = self.ycor() - MOVE_DISTANCE
		if new_y > -280:  # Check if the new y-coordinate is within bounds
			self.goto(self.xcor(), new_y)
