
#https://ivtipm.github.io/Programming/Glava01/index01.htm#z2
#Даны действительные числа x и y. Получить (|x| - |y|) / (1 + |xy|)

__author__ ='Borisova Ekaterina IVT20'


import math as m
import mth

assert 0 ==mth.calc1(1, 1)
assert -0.03225806451612903 ==mth.calc1(5, 6)
assert 0.21428571428571427 ==mth.calc1(-9, 3)

x = float (input("Введите x: "))
y = float (input("Введите y: "))

result = mth.calc1(x, y)

print (f"Результат  {result: .3f}")
#.3f

