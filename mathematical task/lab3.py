#https://ivtipm.github.io/Programming/Glava03/index03.htm#z64
#Дано натуральное число n (n > 99). 
#Определить число сотен в нем.

__author__ = 'Borisova Ekaterina IVT20'

import mth

assert mth.calc3(543) == 5
assert mth.calc3(1562) == 15
assert mth.calc3(19512) == 1956


n =int(input ("Введите число больше 99: "))

print(f"В {n} количество сотен равно {mth.calc3(n)} ")

