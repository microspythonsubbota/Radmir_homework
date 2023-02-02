import requests, json, re
from bs4 import BeautifulSoup
from pprint import pprint
import unicodedata
import html5lib

CATEGORY = 'sport'
HOST = 'https://www.gazeta.ru/'
URL = HOST + CATEGORY
HEADER = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"}

site = requests.get(URL, headers=HEADER).text
soup = BeautifulSoup(site, 'html.parser')
articles = soup.find_all('div', class_='row')

json_data=[]

for article in articles:
    titles = article.find('div', class_='b_ear-title')
    pub_times = article.find('time', class_='b_ear-time')
    intro = article.find('div', class_='b_ear-intro')
    images = article.find('div', class_='b_ear-image')
    try:
        pub_time = pub_times.get_text(strip=True)
        intro_f = intro.get_text(strip=True)
        title = titles.get_text(strip=True)
        image = images.find('img').get('src')
        json_data.append({
            'title': unicodedata.normalize("NFKD", title),
            'description': unicodedata.normalize("NFKD", intro_f),
            'data_pub': unicodedata.normalize("NFKD", pub_time),
            'image_link': unicodedata.normalize("NFKD", image)
        })
    except:
        pass
with open(f'gazeta_{CATEGORY}.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)



