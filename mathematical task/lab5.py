#https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#Даны натуральное число n, действительные числа a1,..., an. Вычислить: д) a1^2 + ... + an^2;

__author__ ="Borisova Ekaterina IVT20"

import mth
import ar


assert mth.calc5([1]) == 1
assert mth.calc5([1, 2]) == 5
assert mth.calc5([1, 2, 3]) == 14
assert mth.calc5([5, 7, 6, 6, 13]) == 315

n =int(input ("Введите количество элементов в массиве: "))

a=[]
#a = (ar.ar_filling(a))
a = (ar.ar_filling(a, n))

print(a)
print(f"Результат равен: {mth.calc5(a)}")
