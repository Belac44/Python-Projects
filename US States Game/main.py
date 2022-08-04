import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen_write = turtle.Turtle()

df = pd.read_csv("50_states.csv")
states = [state.lower() for state in df['state'].to_list()]
states_x = df['x'].to_list()
states_y = df['y'].to_list()

print(states)

game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="Guess another state's name")

    if answer_state == "exit":
        print("Learn these states:", states)
        break

    if answer_state.lower() in states and score != 50:
        score += 1
        index = states.index(answer_state.lower())
        screen_write.penup()
        screen_write.goto(states_x[index], states_y[index])
        screen_write.hideturtle()
        screen_write.write(f"{answer_state.upper()}", font=("Arial", 5, "bold"))
        states.remove(states[index])
        states_x.remove(states_x[index])
        states_y.remove(states_y[index])

    if score == 50:
        screen_write.goto(-100, 0)
        screen_write.write("Congratulations, You did it", font=("Arial", 25, "normal"))
        game_is_on = False




screen.exitonclick()

