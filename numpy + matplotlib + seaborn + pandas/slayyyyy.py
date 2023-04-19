__author__ ="Borisova Ekaterina IVT20"

import numpy as np


def Kram(coefficient_matrix, free_terms_vector):
    ""'для вычисления каждой неизвестной нужно заменить соответствующий столбец матрицы коэффициентов вектором свободных членов и поделить определители двух матриц'""
    determinant = np.linalg.det(coefficient_matrix)  #определитель матрицы коэффициентов
    result = list()
    for i in range(len(coefficient_matrix)):
        intermediate_matrix = np.copy(coefficient_matrix)    #вспомогательная матрица(копия матрицы коэффициентов)
        intermediate_matrix[:,i] = free_terms_vector    #: - берем все строки, i - берем i-й столбец, присваиваем вектор свободных членов
        result.append(np.linalg.det(intermediate_matrix)/determinant)   #находим определитель вспомогательной матрицы, делим его на определитель основной матрицы, это и есть рещение
    return result


coefficient_matrix = np.array([[15, 25, 35], [9, 8, 7], [18, 12, 10]])   #матрица коэфициентов
free_terms_vector = np.array([12, 13, 14])  #вектор свободных членов

#метод solve
X = np.linalg.solve(coefficient_matrix, free_terms_vector)   #вектор с решением
print('Метод solve')
print(f'Ответ  = {X}')

#метод обратной матрицы
inverse_matrix = np.linalg.inv(coefficient_matrix)   #отратная матрица
X2 = np.matmul(inverse_matrix,free_terms_vector)    #вектор с решением       умножение ом на всч
print('Метод отбатной матрицы')
print(f'Ответ = {X2}')

#метод Крамора
X3 = Kram(coefficient_matrix, free_terms_vector)
print('Метод Крамора')
print(f'Ответ = {X3}')



