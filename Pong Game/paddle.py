from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.create_shape()

    def create_shape(self):
        self.shape("square")
        self.shapesize(3, 1)
        self.color("white")
        self.penup()
        self.goto(self.pos, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
