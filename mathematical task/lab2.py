#https://ivtipm.github.io/Programming/Glava02/index02.htm#z43
#Даны три действительных числа. 
#Возвести в квадрат те из них, значения которых неотрицательны.

__author__ ='Borisova Ekaterina IVT20'

import mth
import ar

assert mth.calc2([-6, 9, -7, 9, -2, -5, -2, 9, -13, 9]) == [-6, 81, -7, 81, -2, -5, -2, 81, -13, 81]
assert mth.calc2([10, -3, 5, 0]) == [100, -3, 25, 0]
assert mth.calc2([5, -3, -9]) == [25, -3, -9]

num = []

n = 3

num = (ar.ar_filling_minus(num, n))
    
print(f'Было  {num}')
print(f'Стало {mth.calc2(num)}')