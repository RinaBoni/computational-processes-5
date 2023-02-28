#https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#Даны натуральное число n, действительные числа a1,..., an. Вычислить: д) a1^2 + ... + an^2;

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np

def ar_filling(a, n:int):
    """получет массив и кол-во элементов в нем, заполняет массив и возвращает его"""
    a = np.random.randint(low=0, high=100, size=n)
    return a
def calc(a,n):
    sum = 0
    for i in range(n):
        sum =sum + a[i]**2
    return sum

