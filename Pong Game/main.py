from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Arcade Pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()

score1 = ScoreBoard(-100)
score2 = ScoreBoard(100)

screen.update()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -279 or ball.ycor() > 279:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and  ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed("fast")

    if ball.xcor() > 380:
        ball.reset_position()
        score1.increase()

    if ball.xcor() < -380:
        ball.reset_position()
        score2.increase()


screen.exitonclick()
