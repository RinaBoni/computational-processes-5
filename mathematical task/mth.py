#модуль с математическими функциями для заданий 5-8

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np
import math as m


def calc1(x, y):
    result = (m.fabs(x) - m.fabs(y)) / (1 + m.fabs(x*y))
    return result


def calc5(a):
    """вычисляет a1^2 + ... + an^2"""
    sum = 0
    for i in range(len(a)):
        sum =sum + a[i]**2
    return sum

def calc6(a):
    """возвращает элементы из списка а, которые кратные 3 и не кратные 5;"""
    b=[]
    for i in range(len(a)):
        if (a[i] % 3 == 0) and (a[i] % 5 != 0):
                
            b.append(a[i])
            
    return b

def calc7(n, m):
    """вычисляет сумму то 1 до n сумм от 1 до m 1/(i+j**2)"""
    sum =  0

    for i in range (1, n+1):
        for j in range (1, m+1):
            sum = sum + 1 / (i + j ** 2)
            #print (f"При i = {i} и j = {j} сумма равна {sum:.4f}")
    return sum

def calc8(a, matrix):
    """Заменить нулями в матрице те элементы с чётной суммой индексов, для которых имеются равные среди a1, ..., a10."""
    
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            for k in range (len(a)):
                if (matrix[i][j] == a[k]) and ((i+j)%2==0):
                    matrix[i][j] =0
                    print(f"Изменен элемент с индексами ({i}, {j})")
            
    return matrix

def calc8_2(a, matrix):
    """Заменить нулями в матрице те элементы с чётной суммой индексов, для которых имеются равные среди a1, ..., a10."""
    for i in range (len(matrix)):
        if (i%2)==0:
            start = 0
        else:
            start = 1
        for j in range (start, len(matrix), 2):
            if matrix[i][j] in a:
                matrix[i][j] = 0
                #print(f"Изменен элемент с индексами ({i}, {j})")
            
    return matrix