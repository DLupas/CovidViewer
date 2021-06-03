from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    province = db.Column(db.String(100), default = '')
    cases = db.Column(db.Integer, default = 0)
    
    def __repr__(self):
        return province

class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    province = db.Column(db.String(100))
    number_hospitals = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return province, number_hospitals

#this must be below the models
db.create_all()
#this prevents the table from filling up again with the data every time the server is initialized
if (Hospitals.query.first() == None): 
    with open('covidviewer/canada_hospitals_provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            new_entry = Hospitals(province=row[0], number_hospitals=row[1])
            db.session.add(new_entry)
        db.session.commit()
    csv_file.close()

from covidviewer import routes

if __name__ == "__main__":
    app.run(debug=True)