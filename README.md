# computational-processes-6 - Теория вычислительных процессов

[Успеваемость](https://docs.google.com/spreadsheets/d/1HYFkxtTxYqXsZASsX_ZGsDWGBvevukQZhHgS5r-YzW4/edit#gid=1704187175)

[Задания](https://github.com/ivtipm/ProcessCalculus/blob/master/plans/2023/plan.md#домашнее-задание)

## mathematical task - математические задачи

* Дописать тесты

## scraping - скрапинг по сайту забгу

Создайте программу, которая записывает заголовки новостей (публикаций, постов) с выбранного вами сайта (например Новости ЗабГУ или Хабр). Программа должна просматривать несколько десятков страниц сайта. Напишите комментарии, документацию, разбейте программу на функции. Дополнительные баллы, если сохраняете данные в Pandas DataFrame и: - программа сохраняет дату и теги новости +1 - программа сохраняет текст новости +1 Для получения данных со страницы используйте библиотеку `requests`

Результат хранится в `news.csv`

[про скапинг](https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov/)

## numpy + matplotlib + seaborn + pandas
[про heatmap](https://www.codecamp.ru/blog/seaborn-heatmap/)
   
   - [X] создать случайную матрицу numpy array
   - [X] решить СЛАУ (numpy)
   - [X] построить тепловую карту на основе созданной матрицы
   - [X] превратть матрицу в массив, построить гистограмму (seaborn)
   - построить график любой сложной функции. построить график этой же функции с добавлением шума (numpy, matplotlib)[шум](https://habr.com/ru/articles/588270/);   [шум](https://habr.com/ru/articles/342906/)  не забудьте подпис к 
       - [X] подписи к осям, 
       - [X] заголовок графика, 
       - [X] легенду, 
       - координатную сетку
   - *дополнительно*: постройте графики выявленых заражений COVID-19 и смертности для нескольких стран
        - данные https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths
        - подсказка: используте библиотеку pandas
        - можно предложить свой набор данных для графика
