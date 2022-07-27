from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, 'normal'))
        self.hideturtle()

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, 'normal'))
