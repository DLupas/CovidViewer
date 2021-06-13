from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import csv, urllib.request
from covidviewer import daily_parser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.sqlite3' #sets sql database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #removes an error message
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100)) #100 is string length limit
    region = db.Column(db.String(100))
    date = db.Column(db.String(100))
    #date = db.Column(db.DateTime)
    cases_today = db.Column(db.Integer, default = 0)
    cumulative_cases = db.Column(db.Integer, default = 0)
    deaths_today = db.Column(db.Integer, default = 0)
    cumulative_deaths = db.Column(db.Integer, default = 0)
    
    def __repr__(self):
        return name, cases

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
    app.run(debug=True) #debug reloads the server when changes are made 