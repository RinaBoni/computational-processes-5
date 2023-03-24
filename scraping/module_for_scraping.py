#модуль с функциями для скрапинга

__author__ ="Borisova Ekaterina IVT20"

from bs4 import BeautifulSoup   #Beautiful Soup — это Python библиотека для скрапинга данных сайтов через HTML код.
import requests     #Чтобы делать запросы, установите requests (библиотеку для отправки HTTP запросов)
import pandas as pd #для работы с данными
from time import sleep



def all_pages(max_pages, url):
    """скрапинг max_pages страниц по url ссылке с изменение номера в страницы в конце ссылки"""
    map = {}
    #id = 0

    for p in range(max_pages):
    
        #изменение номера страницы
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

        #заносим полученное со страницы в словарь
        news_div_to_map(all_news, map)
        
    return map



def news_div_to_map(all_news, map):
    """заносим полученное со страницы в словарь"""
    id = 0

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
        map[id]["tegs"] = tegs_ready
        map[id]["headline"] = headline
        map[id]["date"] = date



def map_to_list(map, result):
    """проходимся по мапе и заносим данные из нее в список"""
    #индекс списка
    cur_row = 0

    #проходимся по мапе и заносим данные из нее в список
    for id in map.keys():
        result.append([])
        result[cur_row].append(str(map[id]["tegs"]))
        result[cur_row].append(str(map[id]["headline"]))
        result[cur_row].append(str(map[id]["date"]))

        cur_row += 1

    return result



def to_dataframe(result):
    """заносим все в датафрейм и в csv файл"""
    #заносим все в датафрейм
    df = pd.DataFrame(result, columns = ["tegs", "headline", "date"])
    #создаем файл csv
    filename = 'news.csv'
    #заносим датафрейм в csv файл
    df.to_csv(filename)