#работа со списком

__author__ ="Borisova Ekaterina IVT20"

import random

def fill_old(listd:list, n:int):
    """заполнение списка"""
    for i in range(n*n):
        listd.append(random.randint(0,100))
    return listd


def fill(n:int):
    """заполнение списка"""
    listd = []
    for i in range(n*n):
        listd.append(random.randint(0,100))
    return listd

def to_matrix(listd:list, n:int):
    """список переводим в вид матрицы"""
    #индекс списка
    k = 0
    #матрица, которую будем заполнять
    matrix = []
    #заполняем строки
    for i in range(n):
        #столбцы
        col = []
        #заполняем столбцы
        for j in range (n):
            #из списка заносим элементы
            col.append(listd[k])
            k += 1
        #заносим полностью строку
        matrix.append(col)
    return matrix


def multiplication (A, B, n):
    """умножение списков"""
    #объявляем список, в котором мы будем хранить умножение двух матриц
    mul = []
    #заполняем его нулями
    for k in range (n*n):
        mul.append(0.)
    #переводим список в вид матрицы
    mul = to_matrix(mul, n)
    #умножаем
    for row in range(n):
        for col in range(n):
            for i in range(n):
                mul[row][col] += A[row][i] * B[i][col]
    return mul
