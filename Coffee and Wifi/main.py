from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField, URLField
from wtforms.validators import DataRequired
import csv
import codecs

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = URLField(label="Location URL", validators=[DataRequired()])
    open_time = TimeField(label="Open Time", validators=[DataRequired()])
    closing_time = TimeField(label="Closing Time", validators=[DataRequired()])
    wifi_rating = SelectField(label="WiFi Rating", choices=[("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪")], validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices=[("☕"), ("☕☕"), ("☕☕☕"), ("☕☕☕☕"), ("☕☕☕☕☕")], validators=[DataRequired()])
    power_rating = SelectField(label="Power Outlet Rating Fields", choices=[("🔌"), ("🔌🔌"), ("🔌🔌🔌"), ("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')

#-------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        name = form.cafe.data
        location = form.location_url.data
        opening = form.open_time.data
        close = form.closing_time.data
        wifi = form.wifi_rating.data
        coffee = form.coffee_rating.data
        power = form.power_rating.data

        with codecs.open("cafe-data.csv", "a", encoding="utf8", errors='replace') as file:
            file.write(f"\n{name},{location},{opening},{close},{coffee},{wifi},{power}")

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with codecs.open('cafe-data.csv', encoding="utf8", errors='replace') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')

        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
