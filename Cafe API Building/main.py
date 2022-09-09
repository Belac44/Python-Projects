from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    random_cafe = Cafe.query.get(randint(1, 10))

    return jsonify(
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        has_seats=random_cafe.seats,
        has_toilets=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price,
    )


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def search():
    loc = request.args.get("loc")
    cafes = db.session.query(Cafe).all()

    for cafe in cafes:
        if cafe.location == loc:
            return jsonify(cafe=cafe.to_dict())

    return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location"}})


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    try:
        db.session.commit()
    except IntegrityError:
        pass
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:ids>", methods=["PATCH"])
def update_cafe(ids):
    new_price = request.args.get("new_price")
    cafe_to_update = Cafe.query.get(ids)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        try:
            db.session.commit()
        except IntegrityError:
            pass
        return jsonify(response={"success": "Successfully updated the price."})
    return jsonify(response={"error": {"Not Found": "Cafe with that id not found in the database"}})

## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:ids>", methods=["DELETE"])
def delete_cafe(ids):
    key = request.args.get("api_key")
    if key == "123456789":
        cafe_to_delete = Cafe.query.get(ids)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            try:
                db.session.commit()
            except IntegrityError:
                pass
            return jsonify(response={"Sucess": "Cafe deleted"})
        return jsonify(response={"Error": {"Not Found": "Cafe with this id not found"}})
    return jsonify(response={"Error": {"Invalid API KEY": "Check your API Key"}})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
