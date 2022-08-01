from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = 5

    def create_new_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            start_y = random.randint(-250, 250)
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.goto(310, start_y)
            self.all_cars.append(car)

    def move(self):
        if self.all_cars:
            for cars in self.all_cars:
                cars.backward(self.move_distance)
    def restart(self):
        self.all_cars = []





