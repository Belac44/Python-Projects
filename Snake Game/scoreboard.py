from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couriers", 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_text()
        self.hideturtle()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_text()
