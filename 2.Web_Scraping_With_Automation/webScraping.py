#Use Beautiful Soup for automating web Scraping
import requests
from bs4 import BeautifulSoup
url="https://www.geeksforgeeks.org/"
response= requests.get(url, headers={"Accept": "text/html"})
parsed_response = BeautifulSoup(response.text, 'html.parser')
print(parsed_response.prettify())

 