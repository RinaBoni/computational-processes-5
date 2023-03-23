from bs4 import BeautifulSoup   #Beautiful Soup — это Python библиотека для скрапинга данных сайтов через HTML код.
import requests     #Чтобы делать запросы, установите requests (библиотеку для отправки HTTP запросов)
import re   #Регулярные выражения
from re import sub  #Ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.
from decimal import Decimal #Модуль decimal обеспечивает поддержку быстрой арифметики с правильно округленным десятичным числом с плавающей запятой.
import io   #предоставляет основные средства Python для работы с различными типами ввода/вывода
from datetime import datetime   #позволяет управлять датами и временем, представляя их в таком виде, в котором пользователи смогут их понимать.
import pandas as pd #для работы с данными
from time import sleep

#поисе в определенной зоне
url = 'https://zabgu.ru/php/news.php?category=1&page='

#находит теги первой новости
#news = soup.find('div', class_ = 'preview_new')
#tegs = news.find('div', class_ = 'markersContainer').text

map = {}
id = 0

#максимальное количество страниц
max_pages = 100

for p in range(max_pages):
    
    cur_url = url + str(p + 1)

    print("Скрапинг страницы №: %d" % (p + 1))

    #делаем запрос и получаем html
    html_text = requests.get(cur_url).text

    #делаем задержки, чтобы не перегружать сервер сайта
    #sleep(3)

    #используем парсер lxml
    #lxml – это библиотека, которая позволяет легко обрабатывать XML и HTML файлы, а также может использоваться для парсинга веб-страниц
    #переменная soup содержит полный html-код страницы
    soup = BeautifulSoup(html_text, 'lxml')
    
    #находит все новости
    all_news = soup.find_all('div', class_ = 'preview_new')

    
    #проходимся по всем новостям
    for i in range(len(all_news)):

        news = all_news[i]  #в news заносим новость с индексом i
        id += 1
        map[id] = {}

        
        tegs = news.find('div', class_ = 'markersContainer').text   #в tegs заносим теги
        headline = news.find('div', class_ = 'headline').text   #в headline заносим превью новости
        dm = news.find('p', class_ = 'day').text   #в day заносим день и месяц публикации
        year = news.find('p', class_ = 'yearInTileNewsOnPageWithAllNews').text  #в year заносим год публикации

        #удаляем перенос строки из тегов
        tegs_ready = tegs.replace('\n', ' ')
        #соеденяем строки
        date = " ".join([dm, year])

        #заносим в мапу
        #map[id]["id"] = id
        map[id]["tegs"] = tegs_ready
        map[id]["headline"] = headline
        map[id]["date"] = date

#список с результатом
result = []
#индекс списка
cur_row = 0

#проходимся по мапе и заносим из нее в список
for id in map.keys():
    result.append([])
    #result[cur_row].append(int(map[id]["id"]))
    result[cur_row].append(str(map[id]["tegs"]))
    result[cur_row].append(str(map[id]["headline"]))
    result[cur_row].append(str(map[id]["date"]))

    cur_row += 1

#заносим все в датафрейм
#df = pd.DataFrame(result, columns = ["news_id", "tegs", "headline", "date"])
df = pd.DataFrame(result, columns = ["tegs", "headline", "date"])

#создаем файл csv
filename = 'news.csv'
#заносим датафрейм в csv файл
df.to_csv(filename)

print("Готово!")








