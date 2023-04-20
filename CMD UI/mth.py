#модуль с математическими функциями для задания 5

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np

def calc5(a):
    """вычисляет a1^2 + ... + an^2"""
    #сумма
    sum = 0
    #проходимя по  массиву
    for i in range(len(a)):
        #считаем сумму
        sum =sum + a[i]**2
    #возвращаем сумму
    return sum

def ar_filling(n:int):
    """создает, дает заполнить руками список и возвращает его"""
    #создаем список
    a = []
    #проходимся по нему
    for i in range(0, n):
        #заполняем список
        a.append(int(input(f"Введите {i+1}-е число: ")))
    #возвращаем список
    return a
