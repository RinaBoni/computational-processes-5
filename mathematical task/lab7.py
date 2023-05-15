#https://ivtipm.github.io/Programming/Glava10/index10.htm#z334
# Вычислить:
#сумма то 1 до 100 сумм от 1 до 50 1/(i+j**2)

__author__ ="Borisova Ekaterina IVT20"

import mth

assert round(mth.calc7(2, 2), 2) == 1.2
assert round(mth.calc7(3, 2), 2) == 1.59
assert round(mth.calc7(1, 1), 2) == 0.5

n = 100
m = 50

print(f'Сумма то 1 до {n} сумм от 1 до {m} 1/(i+j**2) равна: {mth.calc7(n, m):.4f}')
