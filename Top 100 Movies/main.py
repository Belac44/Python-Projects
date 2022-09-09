from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy.exc import IntegrityError
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

API_ENDPOINT = "https://api.themoviedb.org/3"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api_movie_list = []


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
db.session.add(new_movie)

try:
    db.session.commit()
except IntegrityError:
    pass


class MyForm(FlaskForm):
    rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    button = SubmitField("Done")

class AddForm(FlaskForm):
    movie = StringField("Movie Title:", validators=[DataRequired()])
    button = SubmitField("Done")

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET","POST"])
def edit():
    edit_form = MyForm()
    if edit_form.validate_on_submit():
        rating_input = edit_form.rating.data
        review_input = edit_form.review.data

        movie_id = request.args.get("id")
        movie_to_edit = Movie.query.get(movie_id)
        movie_to_edit.rating = rating_input
        movie_to_edit.review = review_input

        try:
            db.session.commit()
        except IntegrityError:
            pass
        return redirect(url_for('home'))

    return render_template("edit.html", form=edit_form, )

@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    try:
        db.session.commit()
    except IntegrityError:
        pass
    return redirect(url_for('home'))


@app.route("/add", methods = ["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_input = add_form.movie.data
        params = {
            "api_key": os.environ["API_KEY"],
            "query": movie_input,
            "language": "en-US",
            "page": 1,
            "include_adult": "true",
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/multi", params=params)
        global api_movie_list
        api_movie_list = response.json()["results"]

        return render_template("select.html", movies=api_movie_list)
    return render_template("add.html", form=add_form)


@app.route("/add_from_search/<int:movie_id>")
def add_from_search(movie_id):
    for movie in api_movie_list:
        if movie['id'] == movie_id:
            print(movie)
            new_movie = Movie(
                title=movie.get('original_name') or movie.get('original_title'),
                year=movie.get('release_date') or movie.get("first_air_date"),
                description=movie.get("overview"),
                rating=0,
                ranking=10,
                review="",
                img_url=f"https://image.tmdb.org/t/p/w500/{movie.get('poster_path')}"
            )
            db.session.add(new_movie)
            try:
                db.session.commit()
            except IntegrityError:
                pass

    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

