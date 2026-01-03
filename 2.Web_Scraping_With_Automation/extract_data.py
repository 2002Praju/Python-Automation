import requests
from bs4 import BeautifulSoup
url="https://www.geeksforgeeks.org/"
respionse= requests.get(url, headers={"Accept": "text/html"})
parsed_response = BeautifulSoup(respionse.text, 'html.parser')
titles = parsed_response.find_all('h2', class_='entry-title')
for title in titles:
    print(title.get_text())
    