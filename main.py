import requests
from bs4 import BeautifulSoup

# IP
link = "https://2ip.ru/"
response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = "d_clip_button")

cheack_js = block.find("span").text
# IP END

# Имя ПК
soup = BeautifulSoup(response, 'lxml')

right_block = soup.find('div', class_='data_item')
name_of_pc = right_block.find_all("div", class_="ip-icon-label")[0].text

# Имя ПК END

# Местоположение
soup = BeautifulSoup(response, 'lxml')
mesto = soup.find_all('div', class_='data_item copy-info-details')[3]
mestoIs = mesto.find_all('div', class_='value value-country')[0].text
# Местоположение END

# Местоположение
soup = BeautifulSoup(response, 'lxml')
provayder = soup.find_all('div', class_='data_item copy-info-details')[4]
provayderIs = provayder.find_all('a')[0].text
# Местоположение END


print('Ваш IP: ',cheack_js)
print('Имя вашего компьютера: ',name_of_pc)
print('Ваше местоположение: ',mestoIs)
print('Ваш провайдер: ',provayderIs)