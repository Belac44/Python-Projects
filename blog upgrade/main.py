from flask import Flask, render_template, request
import requests

app = Flask(__name__)
posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

@app.route('/')
def get_index():
    return render_template('index.html', posts =posts)

@app.route("/posts/<int:post_num>")
def get_post(post_num):
    return render_template("post.html", post=posts[post_num])

@app.route("/contact", methods=["GET",'POST'])
def get_contact():
    if request.method == "GET":
        return render_template("contact.html", hh1="Contact Me")
    elif request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print(f"{name}\n{email}\n{phone}\n{message}")

        return render_template("contact.html", hh1="Successfully sent your message")


@app.route("/about")
def get_about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')