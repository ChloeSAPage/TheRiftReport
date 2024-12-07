import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.leagueoflegends.com/en-us/news/game-updates/patch-14-23-notes/')

# check status code for response received
# success code - 200
print(r)
print(r.text)
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
s = soup.find('div', id='patch-notes-container').get_text("|", strip=True)
# print(s)