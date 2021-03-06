'''
 -----------------------------------------------------
 Name:             __init__
 Purpose:          Run when the flask application is created, initializes the application
 Author:           Daniel Lupas
 Updated:          18-Jun-2021
 References:       Past cases and deaths data taken from https://opencovid.ca's open project at https://raw.githubusercontent.com/ccodwg/Covid19Canada/master
                   Hosptial data taken from: https://www.ic.gc.ca/app/scr/app/cis/businesses-entreprises/622?wbdisable=true
 ----------------------------------------------------
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import csv, urllib.request
from covidviewer import daily_parser

app = Flask(__name__) #create instance of flask class
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.sqlite3' #sets sql database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #removes an error message
db = SQLAlchemy(app) #create SQLAlchemy database

class PastData(db.Model): #model for the past data on the past page
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100)) #100 is string length limit
    region = db.Column(db.String(100))
    date = db.Column(db.String(100))
    #date = db.Column(db.DateTime) 
    cases_today = db.Column(db.Integer, default = 0)
    cumulative_cases = db.Column(db.Integer, default = 0)
    deaths_today = db.Column(db.Integer, default = 0)
    cumulative_deaths = db.Column(db.Integer, default = 0)
    
    #defines how the entry is outputted when you print it to console among other things
    '''
    def __repr__(self):
        return self.name, self.cases 
    '''

class Hospitals(db.Model): #model for the daily data on the today page
    id = db.Column(db.Integer, primary_key = True)
    province = db.Column(db.String(100))
    number_hospitals = db.Column(db.Integer, default = 0)

    '''
    def __repr__(self):
        return self.province, self.number_hospitals
    '''

#this must be below the models
db.create_all()
#this prevents the table from filling up again with the data every time the server is initialized
if (Hospitals.query.first() == None): 
    #read hospitals data from csv
    with open('covidviewer/canada_hospitals_provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            new_entry = Hospitals(province=row[0], number_hospitals=row[1])
            db.session.add(new_entry)
        db.session.commit()
    csv_file.close()

#checks the date of the last update
lastUpdated = "01-01-2020" #date before any entries
if PastData.query.first() != None:
    lastUpdated = PastData.query.order_by(PastData.id.desc()).first().date #orders by id, descending, takes only 1

today = datetime.date.today()
date_formatting_style = "%d-%m-%Y" #allows changing the formating style of the date
#.strptime turns a properly formatted string eg. 06-06-2021 into a datetime object
lastUpdated = datetime.datetime.strptime(lastUpdated, date_formatting_style)

#not needed, since you can compare datetime objects 
#str_today = today.strftime(date_formatting_style) #strftime reformates datetime object and converts to string
#print(lastUpdated)

if lastUpdated < datetime.datetime.today(): #if the csv file has been updated since the database last was updated
    #populate the past database with information, only update with what is new
    #using data from https://opencovid.ca
    #2 seperate csv files must be opened seperately 
    cases_database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/cases_timeseries_hr.csv"
    deaths_database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/mortality_timeseries_hr.csv"
    cases_response = urllib.request.urlopen(cases_database_url)
    deaths_response = urllib.request.urlopen(deaths_database_url)

    cases_lines = []
    cases_discard = cases_response.readline() #discard first line as it is the column names
    for line in cases_response.readlines():
        #turn binary into string
        new_line = line.decode()
        cases_lines.append(new_line)
    cases_csv_file = csv.reader(cases_lines)

    #since there are 2 csv files to read, repeat the process
    deaths_lines = []
    deaths_discard = deaths_response.readline()
    for line in deaths_response.readlines():
        deaths_lines.append(line.decode())
    deaths_csv_file = csv.reader(deaths_lines)

    #turn into list instead of csv.reader object
    deaths_by_row = []
    for line in deaths_csv_file: 
        if line[1] != "Not Reported": #remove "Not Reported" lines
            deaths_by_row.append(line)

    deaths_itterator = 0 #there are a different number of lines in the deaths csv file
    #because deaths start in March instead of January so this is used to match the lines up together
    for row in cases_csv_file:
        #there are some "Not Reported" entries that need to be filtered out
        #turns the date of the entry into an datetime object, then compares it with the date last updated to see if it's recent
        #new entries will not in order with entries from the same region, but when querying the database shouldn't matter
        if row[1] != "Not Reported" and datetime.datetime.strptime(row[2], date_formatting_style) > lastUpdated:
            deaths_today = 0 #default for these variables is 0
            cumulative_deaths = 0
            
            #province, region and date must match up 
            if deaths_by_row[deaths_itterator][0] == row[0] and deaths_by_row[deaths_itterator][1] == row[1] and deaths_by_row[deaths_itterator][2] == row[2]:
                deaths_today = deaths_by_row[deaths_itterator][3]
                cumulative_deaths = deaths_by_row[deaths_itterator][4]
                #move onto the next row, this pauses going through the deaths file during Jan and Feb for each region
                deaths_itterator += 1
            
            #create new entry in database
            new_entry = PastData(name=row[0], region=row[1], date=row[2], cases_today=row[3], cumulative_cases=row[4], deaths_today=deaths_today, cumulative_deaths=cumulative_deaths)
            db.session.add(new_entry)
    db.session.commit()

#wipe out data so the past page is blank
with open('covidviewer/static/pastdata.json', 'w') as past_data:
    past_data.write("") 
past_data.close()   

#bottom import avoids circular import error
from covidviewer import routes

if __name__ == "__main__":
    app.run(debug=True) #debug reloads the server when changes are made 