from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couriers", 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_text()
        self.hideturtle()
    def update_text(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.update_text()


    def gameover(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=FONT)