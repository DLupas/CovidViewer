from covidviewer import app, db, PastData, Hospitals
from covidviewer import daily_parser
from flask import render_template, request, make_response
import json

@app.route("/") #homepage
def index():
    return render_template('index.html')

@app.route("/daily") #today's data page
def daily():
    #this page will take a while to load the first time because it creates a web connection to the page
    if not request.cookies.get("daily_data"):
        daily_data = daily_parser.extract() #call extract function from daily_parser file
        res = make_response(render_template('daily.html', daily_data=daily_data))
        res.set_cookie("daily_data", " ".join(daily_data), max_age=60*60*24) #cookie will last 1 day
        return res
    else:
        daily_data = request.cookies.get("daily_data") #retrieve cookie
        daily_data = daily_data.split(" ") #converts string to list
        return render_template('daily.html', daily_data=daily_data)
    
@app.route("/past", methods=['GET', 'POST']) #past data page
def past():
    chosenValue = None
    if request.method == 'POST':
        chosenValue = request.form.get('region', None)
    printout = []

    #read health regions from file
    regions = []
    with open("covidviewer/regions.txt", "r") as regions_file:
        regions = regions_file.readlines()
    regions_file.close()
    
    #printout only the results related to the search
    #add province searches and Canada wide searches
    #add date selection
    #json default nothing
    
    if chosenValue:
        chosenValue = chosenValue.split(":") #splits into list of 2, province and region
        #query sql database

        search_for_region = chosenValue[-1].strip("\n") #these characters interfere with the result and must be removed
        search_for_region = search_for_region.strip("\r")
        print(search_for_region)
        data = PastData.query.filter_by(region=search_for_region) #chosenValue[1] is the region
        for entry in data: #creates a list of all the health regions
            #print(entry)
            '''
            new_region = entry.name + "-" + entry.region
            if new_region not in regions: #if the region is already in the list, don't add it again
                regions.append(new_region)
            '''
            if entry.name == chosenValue[0]: #health region names are not unique, match up with province
                new_line = [entry.name, entry.region, entry.date, str(entry.cases_today), str(entry.cumulative_cases), str(entry.deaths_today), str(entry.cumulative_deaths)]
                printout.append(new_line)
        print(printout)
        with open("covidviewer/static/data.json", "w") as data_file:
            to_file = {} #the dictionary passed to json
            body_values = [] #the list inside the dictionary
            for row in printout:
                new_line = {"date":row[2], "cases":row[3], "deaths":row[5]}
                body_values.append(new_line)
            to_file["covid"] = body_values
            to_file = json.dumps(to_file)
            data_file.write(to_file)
        data_file.close()
    return render_template('past.html', entries=printout, regions=regions, chosenValue=chosenValue)

@app.route("/hospitals") #hospitals map page
def hospitals():
    hospitals_by_province = []
    '''
    #test data
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
    hospitals = Hospitals.query.all() #query sql database 
    for h in hospitals:
        new_line = h.province + ": " + str(h.number_hospitals)
        hospitals_by_province.append(new_line)
    return render_template('hospitals.html', hospitals=hospitals_by_province)

'''
@app.route("/test", methods=['GET', 'POST']) #test page for html forms
def test():
    chosenValue = ""
    if request.method == 'POST':
        chosenValue = request.form.get('region', None)
    return render_template('test.html', chosenValue=chosenValue)
'''