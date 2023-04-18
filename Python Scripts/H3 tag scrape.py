import requests
from bs4 import BeautifulSoup

# specify the URL of the webpage you want to scrape
url = 'https://www.marocannonces.com/categorie/305/Location-immobilier.html'

# make a GET request to fetch the HTML content
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find all the <h3> tags in the HTML content
headings = soup.find_all('h3')

# print the text content of all the <h3> tags
for heading in headings:
    print(heading.text)
