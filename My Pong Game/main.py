from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

ball_speed = 0.1

game_is_on = True
while game_is_on:
	time.sleep(ball.movement_speed)
	screen.update()
	ball.move()

	# Collision detection with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Collision detection with paddle
	if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
		ball.bounce_x()

	# Right paddle miss detection
	if ball.xcor() > 395:
		ball.reset_ball_position()
		scoreboard.l_point()

	# Left paddle miss detection
	if ball.xcor() < -395:
		ball.reset_ball_position()
		scoreboard.r_point()

screen.exitonclick()