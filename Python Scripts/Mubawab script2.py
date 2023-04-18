import requests
from bs4 import BeautifulSoup

url = "https://www.mubawab.ma/fr/sc/appartements-a-louer"

for page_num in range(1, 4):  # scrape the first three pages
    page_url = f"{url}?page={page_num}"
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all listings on the page
    listings = soup.find_all('h2', class_='listingTit')

    # print the text inside the <a> tag for each listing
    for listing in listings:
        a_tag = listing.find('a')
        if a_tag is not None:
            print(a_tag.text.strip())
