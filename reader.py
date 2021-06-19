'''
 -----------------------------------------------------
 Name:             reader
 Purpose:          test file
 Author:           Daniel Lupas
 Updated:          18-Jun-2021
 References:       
 ----------------------------------------------------
'''
'''
from selenium import webdriver
my_url = "https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html"
driver = webdriver.PhantomJS()
driver.get(my_url)
p_element = driver.getElementsByClass('nationalNumbers-data')
print(p_element.text)
'''
'''
import csv, urllib.request

database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/cases_timeseries_hr.csv"
response = urllib.request.urlopen(database_url)
lines = []
for line in response.readlines():
    lines.append(line.decode())
csv_file = csv.reader(lines)

f = open("printout.txt", "w")
for row in csv_file:
    if row[1] != "Not Reported":
        f.write(str(row) + "\n")
'''
'''
data = response.read()
csv_file = csv.reader(data)

for row in csv_file:
    print(str(row))
'''
'''
with open("https://health-infobase.canada.ca/src/data/covidLive/covid19-download.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    limit = 0
    for row in csv_reader:
        if limit < 10:
            print(row)
        else:
            break
'''