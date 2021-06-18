from bs4 import BeautifulSoup
from selenium import webdriver
#selenium is requiered to render javascript 
#The tables on the page are generated dynamically and requests will only get html
from selenium.webdriver.firefox.options import Options
#make the browser opened headless ie. doesn't pop up
import requests
import time

def extract():
    dataURL = "https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html"
    
    #set up headless
    options = Options()
    options.headless = True
    
    #geckodriver must be installed in path to use Firefox
    driver = webdriver.Firefox(options=options)
    driver.get(dataURL)
    #give page time to load
    time.sleep(5)
    page = driver.page_source
    #requests.get() gives straight html
    #page = requests.get(dataURL)
    
    #creates a beautiful soup object that maps the html
    soup = BeautifulSoup(page, "lxml")
    #print(soup.prettify())

    results = []
    #data we want is in tags without a class, so we search for the closest class and narrow it down
    bodyContainer = soup.find(class_="nationalNumbers-data")
    print(bodyContainer)
    for trTag in bodyContainer.find_all("tr"):
        tdTag = trTag.find_all("td")
        for data in tdTag:
            if data.text == "N/A": #turn N/A into 0
                results.append("0")
            elif "," in data.text: 
                removeComma = data.text.replace(",", "")
                results.append(removeComma)
            else:
                results.append(data.text) #.text strips tags 

    driver.close()
    return results
'''
#for testing purposes
with open("page.txt", "w") as page:
    page.write(soup.prettify())
page.close()
'''