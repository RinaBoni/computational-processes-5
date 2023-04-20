#List vs NumPy vs Torch в скорости

__author__ ="Borisova Ekaterina IVT20"

import numpy as np 
import list1
import torch
import time #для замера времени


# размер квадратной матрицы
n = 500





#начало выполнения умножения списков
start = time.time()

#заполняем список А
A_list = list1.fill(n)
#переводим список в вид матрицы
A_list_matrix = list1.to_matrix(A_list, n)

#заполняем список В
B_list = list1.fill(n)
#переводим список в вид матрицы
B_list_matrix = list1.to_matrix(B_list, n)

#выполняем умножение
mul_list = list1.multiplication(A_list_matrix, B_list_matrix, n)

#конец выполнения умножения списков
end = time.time()

#вывод потраченного времени
print('time', end-start)





#начало выполнения умножения матриц numpy
start = time.time()

#заполняем матрицу А
A_np = np.random.randint(low=0, high=100, size=(n,n))

#заполняем матрицу В
B_np = np.random.randint(low=0, high=100, size=(n,n))

#выполняем умножение
mul_np = A_np * B_np

#конец выполнения умножения матриц numpy
end = time.time()

#вывод потраченного времени
print('time', end-start)




#torch.rand(n,n)значения инициализируются из случайного равномерного распределения
#torch.mul(x, y) поэлементное умножение
#начало выполнения умножения тензора torch
start = time.time()

#заполняем тензор А
A_torch = torch.rand(n,n)

#заполняем тензор В
B_torch = torch.rand(n,n)

#выполняем умножение
mul_torch = torch.mul(A_torch, B_torch)

#конец выполнения умножения тензора torch
end = time.time()

#вывод потраченного времени
print('time', end-start)





