import requests
from bs4 import BeautifulSoup

url = 'https://tengrinews.kz//'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

m_titles = soup.find_all('span', class_='tn-main-news-title')

a_titles = soup.find_all('span', class_='tn-article-title')


for m_title in m_titles:
    m_title_text=m_title.text
    print(f'{m_title_text}\n' )

for a_title in a_titles:
    a_title_text=a_title.text
    print(f'{a_title_text}\n' )
