from flask import Flask, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)



##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()
posts = db.session.query(BlogPost).all()

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.subtitle.data,
            date=datetime.now().strftime("%B %d, %Y"),
            author=post_form.author.data,
            img_url=post_form.img_url.data,
            body=post_form.body.data
        )
        db.session.add(new_post)
        try:
            db.session.commit()
        except IntegrityError:
            pass
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", post_form=post_form, read="New Post")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    post_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )
    if post_form.validate_on_submit():
        post.title=post_form.title.data
        post.subtitle=post_form.subtitle.data
        post.author=post_form.author.data
        post.img_url=post_form.img_url.data
        post.body=post_form.body.data
        db.session.commit()

        return redirect(url_for("show_post", index=post_id))
    return render_template("make-post.html", read="Edit Post", post_form=post_form)


@app.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = BlogPost.query.get(id)
    db.session.delete(post_to_delete)
    try:
        db.session.commit()
    except IntegrityError:
        pass
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')