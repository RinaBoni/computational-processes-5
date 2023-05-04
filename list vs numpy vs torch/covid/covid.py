import pandas as pd
import os
import matplotlib.pyplot as plt
__author__ = "Gurbatov"

# чтение файла с данными
# index_col заменяет id на дату
data = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv", index_col='Date_reported', parse_dates=True)
# фильтр по названию страны
def makegraph(data:pd.DataFrame, country:str, type:str, datefrom:str, dateto:str):
    """"Создаёт граф Covid c указаной странной, видом значений(смерти, заражения)..., датой"""
    # создание таблицы с 1 страной
    filtercountry = data['Country'] == country
    # создание таблицы с 1 страной датой и смертностью
    new_sample = data.loc[filtercountry]
    new_sample = new_sample.loc[datefrom:dateto, type]
    new_sample.plot(label=country)
    # вывод названия графиков
    plt.xlabel('Date')
    plt.ylabel(type)
    plt.legend()
    plt.title('Covid-19')
    plt.show()


# вывод графика 
makegraph(data, "Russian Federation", "New_deaths",'2020-01-03','2022-05-27')
makegraph(data, "Mexico", "New_deaths",'2020-01-03','2022-05-27')
makegraph(data, "Zimbabwe", "New_cases",'2020-01-03','2022-05-27')
makegraph(data, "Bangladesh", "New_cases",'2020-01-03','2022-05-27')





