from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.setpos()

    def setpos(self):
        for pos in starting_pos:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.segments.append(new_segment)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(90)
