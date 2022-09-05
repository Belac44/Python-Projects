from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register_user():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    return f"<h1>First name: {fname}, Lname:{lname}, Email:{email}</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
