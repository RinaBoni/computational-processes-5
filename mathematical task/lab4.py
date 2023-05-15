#https://ivtipm.github.io/Programming/Glava04/index04.htm#z114
#Вычислить сумму последовательности i = 1..10, 1/i! 

__author__ ="Borisova Ekaterina IVT20"

import mth

assert round(mth.calc4(10), 3) == 1.718
assert round(mth.calc4(5), 3) == 1.717
assert round(mth.calc4(2), 3) == 1.5

n = 10

mth.calc4(n)
