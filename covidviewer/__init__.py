from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import csv, urllib.request
from covidviewer import daily_parser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.sqlite3' #sets sql database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #removes an error message
db = SQLAlchemy(app)

class PastData(db.Model):
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

cases_database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/cases_timeseries_hr.csv"
deaths_database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/mortality_timeseries_hr.csv"
response = urllib.request.urlopen(cases_database_url)

lines = []
discard = response.readline() #discard first line as it is the column names
for line in response.readlines():
    #turn binary into string
    lines.append(line.decode())
csv_file = csv.reader(lines)

for row in csv_file:
    #there are some not reported entries that need to be filtered out
    if row[1] != "Not Reported":
        new_entry = PastData(name=row[0], region=row[1], date=row[2], cases_today=row[3], cumulative_cases=row[4])
        db.session.add(new_entry)
db.session.commit()

from covidviewer import routes

if __name__ == "__main__":
    app.run(debug=True) #debug reloads the server when changes are made 