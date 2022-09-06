from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    return render_template('index.html', books=db.session.query(Book).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['book'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):

    if request.method == "POST":
        book_to_update = Book.query.get(book_id)

        book_to_update.title = request.form['book']
        book_to_update.author = request.form['author']
        book_to_update.rating = request.form['rating']
        try:
            db.session.commit()
        except IntegrityError:
            pass
        return redirect(url_for('home'))
    return render_template("edit.html", id=book_id, book=Book.query.get(book_id))

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    try:
        db.session.commit()
    except IntegrityError:
        pass
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

