import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd


for page in range(1,17):
    base_url = 'https://www.coldwellbankerhomes.com/'
    url = f'https://www.coldwellbankerhomes.com/ca/arcadia/agents/{page}'

    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    profile_link = []
    all_data = []
    links = soup.findAll('h2', {'class': 'agent-content-name'})
    # print(links)
    for link in links:
        data_link = link.find('a').get('href')
        profile_link.append(base_url + data_link)
        # rint(profile_link)p

    for data in profile_link:
        res2 = requests.get(data)
        soup2 = bs(res2.text, 'html.parser')
        name = soup2.find('h1', {'id': 'main-content'}).text
        email = soup2.find('div', {'class': 'body'}).text
        mobile_number = soup2.find('span', {'itemprop': 'telephone'}).text
        office_number = soup2.find('a', {'class': 'phone-link'}).text
        office_address = soup2.find('span', {'class': 'office-span'}).text
        # description  = soup2.find('div', {'class': 'bio-section'})
        # paragrap = description.find('p')
        final_data = {
            'Name': name,
            'Email': email,
            'Mobile Number': mobile_number,
            'Office Number': office_number,
            'Office Address': office_address,
            # 'Pargrapha': paragrap

        }
        all_data.append(final_data)
        data_2 = pd.DataFrame(all_data)
        print(data_2)

