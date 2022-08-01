import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road Game")
screen.bgcolor("black")
screen.tracer(0)


space = Turtle("square")
space.color("white")
space.shapesize(stretch_len=30, stretch_wid=25)

car = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.create_new_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 250:
        score.increment()
        player.restart()
        car.restart()
        car.move_distance += 5



screen.exitonclick()