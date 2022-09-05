from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inner():
        f"<b>{function()}</b>"
    return inner

@app.route("/")
@make_bold
def welcome_page():
    return "<p>Welcome Home</p>"

@app.route("/bye")
def bye():
    return "<h3>Bye</h3>"

@app.route("/<name>")
def greet(name):
    return f"<h2 style = 'text-align: center'>Hello {name + str(12)}</h2>"

if __name__ == "__main__":
    app.run(debug=True)



