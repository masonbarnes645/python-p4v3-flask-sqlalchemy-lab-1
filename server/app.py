# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here

@app.route('/earthquakes/<int:id>')
def earthquake_by_id(id):
    eq = Earthquake.query.filter_by(id=id).first()
    
    if eq:
     response_body = eq.to_dict()
     response_status = 200
    else:
        response_body = {'message': f'Earthquake {id} not found.' }
        response_status = 404
    response =  make_response = (response_body, response_status)
    return response

@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquake_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude > magnitude).all()
    count = len(earthquakes)
    quakes = [earthquake.to_dict() for earthquake in earthquakes]
    response_body = {
        'count': count,
        'quakes': quakes
    }

    return (response_body)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
