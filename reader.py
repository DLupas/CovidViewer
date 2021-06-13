import csv, urllib.request

database_url = "https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_hr/cases_timeseries_hr.csv"
response = urllib.request.urlopen(database_url)
lines = []
for line in response.readlines():
    lines.append(line.decode())
csv_file = csv.reader(lines)

for row in csv_file:
    print(row)
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