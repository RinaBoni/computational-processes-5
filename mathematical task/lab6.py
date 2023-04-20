#https://ivtipm.github.io/Programming/Glava07/index07.htm#z17810
# последовательности a1,...,an:
#б) кратных 3 и не кратных 5;

__author__ ="Borisova Ekaterina IVT20"

import ar
import mth

assert mth.calc6([6, 9, 14, 9, 15]) == [6,  9, 9]
assert mth.calc6([2, 9, 4, 1]) == [9]
assert mth.calc6([8, 7, 6, 15]) == [6]

n =int(input ("Введите количество элементов в массиве: "))

a=[]

a = (ar.ar_filling(a, n))


print(a)
#print(ar6.calc(a))
print(f"Результат равен: {mth.calc6(a)}")
