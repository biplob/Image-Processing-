import requests
from bs4 import BeautifulSoup as bs
headers = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
url = 'https://www.zoopla.co.uk/find-agents/estate-agents/directory/a/'
res = requests.get(url, headers)
print(res.status_code)
soup = bs(res.text, 'html.parser')

all_links = []
links = soup.findAll('ul', {'class': 'clearfix'})
for link in links:
    data_link = link.find('a').get('href')
    all_links.append(data_link)
print(all_links)