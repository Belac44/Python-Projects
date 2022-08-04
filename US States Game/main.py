import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guesss the state", prompt="What's another state's name?")

screen.exitonclick()

