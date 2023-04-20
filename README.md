# computational-processes-6 - Теория вычислительных процессов

[Успеваемость](https://docs.google.com/spreadsheets/d/1HYFkxtTxYqXsZASsX_ZGsDWGBvevukQZhHgS5r-YzW4/edit#gid=1704187175)

[Задания](https://github.com/ivtipm/ProcessCalculus/blob/master/plans/2023/plan.md#домашнее-задание)
[множества Мандельброта c#](https://www.youtube.com/watch?v=eMSujMjhY0o)
[множества Мандельброта c#](https://www.youtube.com/watch?v=qCgoDEQOSZk&list=PLurO3Bg1TJG9XUNhs3NrM2aQRy2hYWbU3)

## reports - отчеты

## mathematical task - математические задачи







## scraping - скрапинг по сайту забгу

Создайте программу, которая записывает заголовки новостей (публикаций, постов) с выбранного вами сайта (например Новости ЗабГУ или Хабр). Программа должна просматривать несколько десятков страниц сайта. Напишите комментарии, документацию, разбейте программу на функции. Дополнительные баллы, если сохраняете данные в Pandas DataFrame и: - программа сохраняет дату и теги новости +1 - программа сохраняет текст новости +1 Для получения данных со страницы используйте библиотеку `requests`

Результат хранится в `news.csv`

[про скапинг](https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov/)








## numpy + matplotlib + seaborn + pandas

### heatmap.py
[про heatmap](https://www.codecamp.ru/blog/seaborn-heatmap/); [про heatmap](https://datastart.ru/blog/read/seaborn-heatmaps-13-sposobov-nastroit-vizualizaciyu-matricy-korrelyacii)
   - создать случайную матрицу numpy array
   - построить тепловую карту на основе созданной матрицы
### hist.py
   - создать случайную матрицу numpy array
   - превратть матрицу в массив, построить гистограмму (seaborn)
### plot.py
[шум](https://habr.com/ru/articles/588270/);   [шум](https://habr.com/ru/articles/342906/)
   - построить график любой сложной функции
   - построить график этой же функции с добавлением шума (numpy, matplotlib)
   - подписи к осям
   - заголовок графика
   - легенду
   - координатную сетку
###  slayyyyy.py
   - решить СЛАУ (numpy)
### covid.py
   - *дополнительно*: постройте графики выявленых заражений COVID-19 и смертности для нескольких стран
        - данные https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths
        - подсказка: используте библиотеку pandas
        - можно предложить свой набор данных для графика
 
 






## list vs numpy vs torch
Сравните время перемножения двух матриц
- представляя матрицы как списки Python
- представляя матрицы как numpy array
- представляя матрицы как torch tensor (на GPU и CPU)

Чтобы результаты были надёжными, повторите замеры несколько раз. Используйте такие размеры матриц, чтобы перемножение занимало как минимум несколько десятков секунд на CPU.
### list1.py
Работа со списком:
   - заполнение
   - перевод в матрицу
   - умножение
### great_battle.py
Собственно само сравнение

[выполнение на colab](https://colab.research.google.com/drive/1_O1jUjCjIv2QxSEDtWvcmDXlhebAKxLa?usp=sharing)







## CMD UI
Создайте версию программы 5 с командным интерфейсом. Программа должна принимать набор чисел как аргумент программы при запуске.

Можно предложить свой вариант программы с командным интерфейсом.
### CLI.py 
   - основная программа
### mth.py
   - модуль с функциями
