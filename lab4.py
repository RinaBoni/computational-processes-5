#https://ivtipm.github.io/Programming/Glava04/index04.htm#z114
#Вычислить сумму последовательности i = 1..10, 1/i! 

__author__ ="Borisova Ekaterina IVT20"

import math as m

sum =  0

for i in range (10):
    sum = sum + 1 / m.factorial(i+1)
    print (f"При {i+1} сумма равна {sum:.4f}")