from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write_to_screen()

    def write_to_screen(self):
        self.write(f"Level: {self.level}", font=FONT)

    def increment(self):
        self.clear()
        self.level += 1;
        self.write_to_screen()
    def game_over(self):
        self.goto(0, -10)
        self.color("red")
        self.write("Game Over!!", font = FONT)
