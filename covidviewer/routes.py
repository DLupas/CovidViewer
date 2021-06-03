from covidviewer import app, db, Entry, Hospitals
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hospitals")
def hospitals():
    hospitals_by_province = []
    '''
    hospitals_by_province = [
        "Alberta: 175",
        "British Columbia: 139",
        "Manitoba: 81",
        "New Brunswick: 41",
        "Newfoundland and Labrador: 31",
        "Nova Scotia: 47",
        "Northwest Territories: 20",
        "Nunavut: 28",
        "Ontario: 371",
        "Prince Edward Island: 10",
        "Quebec: 224",
        "Saskatchewan: 81",
        "Yukon: 17"
    ]
    '''
    hospitals = Hospitals.query.all()
    for h in hospitals:
        new_line = h.province + ": " + str(h.number_hospitals)
        hospitals_by_province.append(new_line)
    return render_template('hospitals.html', hospitals=hospitals_by_province)