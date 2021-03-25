import requests

from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text
s = 0
k = 0
world = {}
stop = 'a'
while stop != 'Aaaaba':
    s += k
    k = 0
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category').find_all('a')
    wor = names[0].get('title')[:1]
    for name in names:
        stop = name.get('title')
        x = name.get('title')[:1]
        if x == 'Ё':
            x = wor
        if x == wor and stop != 'Aaaaba':
            k += 1
        else:
            s += k
            world[wor] = world.get(wor, 0) + s
            s = 0
            wor = name.get('title')[:1]
            k = 1
        if stop == 'Aaaaba':
            break
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text
            break
for key in sorted(world):
    print(key, world[key], sep=': ')      
