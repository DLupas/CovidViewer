from covidviewer import app, db, PastData, Hospitals
from covidviewer import daily_parser
from flask import render_template, request, make_response
import json
import datetime

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
    
    else:
        daily_data = request.cookies.get("daily_data") #retrieve cookie
        daily_data = daily_data.split(" ") #converts string to list
        res = render_template('daily.html', daily_data=daily_data)

    #list of province codes
    provinces = {"British Columbia": "CA-BC", "Alberta":"CA-AB", "Saskatchewan":"CA-SK", "Manitoba":"CA-MB", "Ontario":"CA-ON", "Quebec":"CA-QC", "Newfoundland and Labrador": "CA-NL", "New Brunswick": "CA-NB", "Nova Scotia": "CA-NS", "Prince Edward Island": "CA-PE", "Yukon": "CA-YT", "Northwest Territorie": "CA-NT", "Nunavut": "CA-NU"}
    '''
    with open("covidviewer/static/dailydata.json", "w") as data_file:
            to_file = {} #the dictionary passed to json
            body_values = [] #the list inside the dictionary
            
            for i in range(0, len(daily_data), 4):
                
                new_line = {"province":provinces[daily_data[i]], "cases":daily_data[i + 1], "deaths":daily_data[i + 2], "testsTaken":daily_data[i + 3]}
                body_values.append(new_line)
            
            to_file["covid"] = body_values
            to_file = json.dumps(to_file)
            data_file.write(to_file)
        
    data_file.close()
    '''
    return res
    
@app.route("/past", methods=['GET', 'POST']) #past data page
def past():
    chosenValue = None
    dateRange = None
    date_formatting_style = "%d-%m-%Y" #used later to convert from one style to another
    
    if request.method == 'POST':
        chosenValue = request.form.get('region', None)
        dateRange = request.form.get('date_picker', None) 
    print(dateRange)
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
        data = PastData.query.filter_by(region=search_for_region) #chosenValue[1] is the region
        
        for entry in data: #creates a list of all the health regions
            #print(entry)
            '''
            new_region = entry.name + "-" + entry.region
            if new_region not in regions: #if the region is already in the list, don't add it again
                regions.append(new_region)
            '''
            if entry.name == chosenValue[0]: #health region names are not unique, match up with province
                if dateRange: #returns all values if no daterange
                    dateRange = eval(str(dateRange)) #eval turns string that looks like dict into dict
                    
                    #convert start and end dates returned from picker to correct format
                    #strptime converts str to datetime object, strf converts datetime to str
                    #convert to datetime object, then convert to string in proper format, then convert back to datetime
                    start_date = datetime.datetime.strptime(dateRange["start"], "%Y-%m-%d")
                    start_date = datetime.datetime.strftime(start_date, date_formatting_style)
                    start_date = datetime.datetime.strptime(start_date, date_formatting_style)
                    
                    end_date = datetime.datetime.strptime(dateRange["end"], "%Y-%m-%d")
                    end_date = datetime.datetime.strftime(end_date, date_formatting_style)
                    end_date = datetime.datetime.strptime(end_date, date_formatting_style)
                
                else:
                    #pick values so that all database entries are included
                    start_date = datetime.datetime.strptime("01-01-2020", date_formatting_style) #date before any entries
                    end_date = datetime.datetime.today() + datetime.timedelta(days=1) #=tomrrow

                entry_date = datetime.datetime.strptime(entry.date, date_formatting_style)
                if start_date <= entry_date <= end_date: #if date within boundaries
                    new_line = [entry.name, entry.region, entry.date, str(entry.cases_today), str(entry.cumulative_cases), str(entry.deaths_today), str(entry.cumulative_deaths)]
                    printout.append(new_line)
        
        with open("covidviewer/static/pastdata.json", "w") as data_file:
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
<<<<<<< Updated upstream
    
    return render_template('hospitals.html', hospitals=hospitals_by_province)


@app.route("/test", methods=['GET', 'POST']) #test page for html forms
def test():
    chosenValue = ""
    if request.method == 'POST':
        chosenValue = request.form.get('region', None)
    res = render_template('test.html', chosenValue=chosenValue)
    return res
=======
    return render_template('hospitals.html', hospitals=hospitals_by_province)


import json
f = open("data1.json", "r")
y = json.loads(f.read())


x = { "province/hospitals" :
    [
        {
            "province" : "Ontario",
            "hospitals": 360
        },
        {
            "province" : "Newfoundland and Labrador",
            "hospitals": 3
        },
        {
            "province" : "Prince Edward Island",
            "hospitals": 23
        },
        {
            "province" : "Nova Scotia",
            "hospitals": 36
        },
        {
            "province" : "New  Brunswick",
            "hospitals": 6
        },
        {
            "province" : "Alberta",
            "hospitals": 5
        },
        {
            "province" : "Quebec",
            "hospitals": 230
        },
        {
            "province" : "British Columbia",
            "hospitals": 7
        },
        {
            "province" : "Yukon",
            "hospitals": 82
        },
        {
            "province" : "Manitoba",
            "hospitals": 33
        },
        {
            "province" : "Northwest Territories",
            "hospitals": 136
        },
        {
            "province" : "Nunavut",
            "hospitals": 236
        },
        {
            "province" : "Saskatchewan",
            "hospitals": 536
        }
    ]
}
y = json.dumps(x)
print(y["province", "hospitals"])
>>>>>>> Stashed changes
