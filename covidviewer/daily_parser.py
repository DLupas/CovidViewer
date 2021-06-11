from bs4 import BeautifulSoup
from selenium import webdriver
#selenium is requiered to render javascript 
#The tables on the page are generated dynamically and requests will only get html
import requests

def extract():
    dataURL = "https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html"
    #geckodriver must be installed in path to use Firefox
    driver = webdriver.Firefox()
    driver.get(dataURL)
    page = driver.page_source
    #requests.get() gives straight html
    #page = requests.get(dataURL)

    #creates a beautiful soup object that maps the html
    soup = BeautifulSoup(page, "lxml")
    #print(soup.prettify())

    results = []
    #data we want is in tags without a class, so we search for the closest class and narrow it down
    bodyContainer = soup.find(class_="nationalNumbers-data")
    for trTag in bodyContainer.find_all("tr"):
        tdTag = trTag.find_all("td")
        for data in tdTag:
            results.append(data.text) #.text strips tags 

    driver.close()
    return results
'''
#for testing purposes
with open("page.txt", "w") as page:
    page.write(soup.prettify())
page.close()
'''