#модуль с математическими функциями для заданий 5-8

__author__ ="Borisova Ekaterina IVT20"

#подключение numpy
import numpy as np

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

def calc7():
    """вычисляет сумму то 1 до 100 сумм от 1 до 50 1/(i+j**2)"""
    sum =  0

    for i in range (1, 10):
        for j in range (1, 6):
            sum = sum + 1 / (i + j ** 2)
            print (f"При i = {i} и j = {j} сумма равна {sum:.4f}")
    return round(sum, 4)

def calc8(a, matrix):
    """Заменить нулями в матрице те элементы с чётной суммой индексов, для которых имеются равные среди a1, ..., a10."""
    
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            for k in range (len(a)):
                if (matrix[i][j] == a[k]) and ((i+j)%2==0):
                    matrix[i][j] =0
                    print(f"Изменен элемент с индексами ({i}, {j})")
            
    return matrix