import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossy Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Check collision with each car
    for car in car_manager.all_cars:
        if car.distance(player) < 21:
            game_is_on = False
            scoreboard.game_over()

    # Check player has reached the finish line
    if player.ycor() == FINISH_LINE_Y:
        player.reset_player_position()
        car_manager.increase_car_speed()
        scoreboard.update_level_score()
        scoreboard.increase_level()

screen.exitonclick()