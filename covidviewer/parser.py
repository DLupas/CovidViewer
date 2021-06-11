from bs4 import BeautifulSoup
from selenium import webdriver
#selenium is requiered to render javascript 
#The tables on the page are generated dynamically and requests will only get html
import requests

dataURL = "https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html"
driver = webdriver.Firefox()
driver.get(dataURL)
page = driver.page_source
#page = requests.get(dataURL)

soup = BeautifulSoup(page, "lxml")
#print(soup.prettify())

bodyContainer = soup.find(class_="nationalNumbers-data")
for trTag in bodyContainer.find_all("tr"):
    #print(trTag)
    data = trTag.find_all("td")
    print(data)

'''
#for testing purposes
with open("page.txt", "w") as page:
    page.write(soup.prettify())
page.close()
'''