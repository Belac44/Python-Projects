from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/guess/<name>")
def welcome_page(name):
    response = requests.get(url="https://api.genderize.io", params={"name": name})
    gender = response.json()["gender"]

    response = requests.get(url="https://api.agify.io", params={"name": name})
    age = response.json()["age"]

    return render_template("index.html", name=name.title(), sex=gender.title(), age=age )


if __name__ == "__main__":
    app.run(debug=True)
