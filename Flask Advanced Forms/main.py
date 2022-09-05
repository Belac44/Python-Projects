from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired, Length
import os


app = Flask(__name__)
app.secret_key = os.environ['SECRET']
Bootstrap(app)

class LogInForm(FlaskForm):
    email = StringField(label="Email: ", validators=[InputRequired("You need to enter your email"),  Email("Enter a valid email address")])
    password = PasswordField(label="Password: ", validators=[InputRequired("You have not entered your password"), Length(min=8, message="Field must be at least 8 characters long")])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():

        input_email = login_form.email.data
        input_password = login_form.password.data

        if input_email == "admin@email.com" and input_password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")