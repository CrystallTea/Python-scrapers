import requests
from bs4 import BeautifulSoup

# Loop for 10 pages
for i in range(1, 11):
    # Define the URL for the page
    url = f'http://www.louervendreaumaroc.com/appartement-maroc/appartement-a-louer-maroc.html?p={i}&amp;chambres=&amp;prix=&amp;q=&amp;a='
    
    # Send a request to the URL and get the response
    response = requests.get(url)
    
    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <li> tags that are inside <ul class="bottom-info-resultat-l-1"> and print their text
    li_tags = soup.select('ul.bottom-info-resultat-l-1 li')
    for li in li_tags:
        print(li.text)
