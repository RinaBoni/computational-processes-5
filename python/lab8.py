#https://ivtipm.github.io/Programming/Glava20/index20.htm#z674
#Даны целые числа a1, ..., a10, целочисленная квадратная матрица
#порядка n. Заменить нулями в матрице те элементы с чётной суммой 
#индексов, для которых имеются равные среди a1, ..., a10.

__author__ ="Borisova Ekaterina IVT20"

import ar
import mth

n =int(input ("Введите количество элементов в квадратной матрице: "))

matrix=[]

a=[]

a = (ar.ar_filling(a, 10))
matrix = (ar.mt_filling(a, n))

print(f'массив а', f'{a}', sep='\n')
print(f"матрица {matrix}")

print (mth.calc8(a, matrix))