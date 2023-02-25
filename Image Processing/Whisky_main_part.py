import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
base_url = 'https://www.thewhiskyexchange.com/'
headers = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
x = 1
all_url = []
url = f'https://www.thewhiskyexchange.com/c/639/bourbon-whiskey?pg={x}'
#all_data = []
while True:
    res = requests.get(url)
    soup = bs(res.content, 'html.parser')
        # data = soup.text
    # print(data)
    links = soup.findAll('li', {'class':  'product-grid__item'})
    for link in links:
        product_link = link.find('a').get('href')
        all_url.append(base_url+product_link)

pg +=1

print(all_url)


    # for data in all_url:
    #     res2 = requests.get(data)
    #     soup2 = bs(res2.text, 'html.parser')
    #     product_name = soup2.find('h1', {'class': 'product-main__name'}).text.replace('\n', "")
    #     ounce = soup2.find('p', {'class': 'product-main__data'}).text.replace('\n', "")
    #     stock = soup2.find('p', {'class': 'product-action__stock-flag'}).text.replace('\n', "")
    #     price = soup2.find('p', {'class': 'product-action__price'}).text.replace('\n', "")
    #     description = soup2.find('div', {'class': 'product-main__description'}).text.replace('\n', "")
    #     review = soup2.find('span', {'class': 'review-overview__count'})
    #     delivery = soup2.find('ul', {'class': 'product-shipping__list'}).text.replace('\n', "")
    #     image_link = soup2.find('div', {'class': 'product-main__image-container'})
    #     image = image_link.find('img').get('src')
    #
    #     final_data = {
    #         'Name' : product_name,
    #         'Ounce' : ounce,
    #         'Stock' : stock,
    #         'Price': price,
    #         'Description' : description,
    #         'Review' : review,
    #         'Delivery' : delivery,
    #         'Image Link': image
    #
    #     }
    #     all_data.append(final_data)
    #     datas = pd.DataFrame(all_data)
    #     datas.to_csv('products.csv', index=False, encoding='utf-8')
