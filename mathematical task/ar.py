#модуль для массивов

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np

#def ar_filling(a:int):
def ar_filling(a, n:int):
    """получет массив и кол-во элементов в нем, заполняет массив и возвращает его"""
    #a = np.random.randint(low=0, high=100, size=len(a))
    a = np.random.randint(low=1, high=15, size=n)
    return a

def mt_filling(a, n:int):
    """получет матрицу и кол-во элементов в ней, заполняет матрицу и возвращает его"""
    #a = np.random.randint(low=0, high=100, size=len(a))
    a = np.random.randint(low=1, high=15, size=(n, n))
    return a