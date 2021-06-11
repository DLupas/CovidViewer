from covidviewer import app, db, Entry, Hospitals
from covidviewer import daily_parser
from flask import render_template, request, make_response

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/daily")
def daily():
    #this page will take a while to load the first time because it creates a web connection to the page
    if not request.cookies.get("daily_data"):
        daily_data = daily_parser.extract() #call extract function from daily_parser file
        res = make_response(render_template('daily.html', daily_data=daily_data))
        str_daily_data = " " #converts list to string
        res.set_cookie("daily_data", str_daily_data.join(daily_data), max_age=60*60*24) #cookie will last 1 day
        return res
    else:
        daily_data = request.cookies.get("daily_data") #retrieve cookie
        daily_data = daily_data.split(" ") #converts string to list
        return render_template('daily.html', daily_data=daily_data)
    


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