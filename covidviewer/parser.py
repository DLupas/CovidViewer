from bs4 import BeautifulSoup
import requests

dataURL = "https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html"
page = requests.get(dataURL)

soup = BeautifulSoup(page.content, "lxml")
print(soup.prettify())