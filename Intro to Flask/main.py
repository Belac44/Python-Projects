from flask import Flask
import random


app = Flask(__name__)

guessed = random.randint(1, 9)


@app.route('/')
def welcome():
    return "<h1>Guess a number between 1 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

@app.route('/<int:guess>')
def guess_input(guess):
    if guess > guessed:
        return "<h1 style='color:purple'>Too high! try again! </p>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    elif guess < guessed:
        return "<h1 style='color:red'>Too low! try again! </p>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    else:
        return "<h1 style='color:green'>You found me!! </p>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"


if __name__ == "__main__":
    app.run()
