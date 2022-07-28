from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, pos):
        self.pos = pos

        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(self.pos, 280)
        self.write_to_screen()

    def write_to_screen(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write_to_screen()