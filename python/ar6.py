#https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
#Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
#б) кратных 3 и не кратных 5;

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np

def ar_filling(a:int):
    """получет массив и кол-во элементов в нем, заполняет массив и возвращает его"""
    a = np.random.randint(low=0, high=16, size=len(a))
    return a

def calc(a):
    """возвращает элементы из списка а, которые кратные 3 и не кратные 5;"""
    b=[]
    for i in range(len(a)):
        if (a[i] % 3 == 0) and (a[i] % 5 != 0):
                
            b.append(a[i])
            
    return b

