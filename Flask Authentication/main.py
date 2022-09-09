from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET',  'POST'])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        new_user = User(
            name=name,
            email=email,
            password=generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        )
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            pass
        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error=None
    if request.method == "POST":
        email_input = request.form.get("email")
        password_input = request.form.get("password")

        user = User.query.filter_by(email=email_input).first()

        if user and check_password_hash(user.password, password_input):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for("secrets"))
        else:
            error = "Invalid email or password"
    return render_template("login.html", message=error)


@app.route('/secrets')
@login_required
def secrets():

    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(path=filename, directory="static/files", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
