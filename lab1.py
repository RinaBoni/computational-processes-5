#https://ivtipm.github.io/Programming/Glava01/index01.htm#z2
#Даны действительные числа x и y. Получить (|x| - |y|) / (1 + |xy|)

__author__ ='Borisova Ekaterina IVT20'


import math as m

x = float (input("Введите x: "))
y = float (input("Введите y: "))

result = (m.fabs(x) - m.fabs(y)) / (1 + m.fabs(x*y))
print (f"Результат  {result: .3f}")

