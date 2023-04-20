#https://ivtipm.github.io/Programming/Glava10/index10.htm#z334
# Вычислить:
#сумма то 1 до 100 сумм от 1 до 50 1/(i+j**2)

__author__ ="Borisova Ekaterina IVT20"

import mth

assert mth.calc7(59, 50) == 18.4501009215536
assert mth.calc7(65, 33) == 18.836715542287997
assert mth.calc7(40, 90) == 15.124518829762762

n = 100
m = 50

print(f'Сумма то 1 до {n} сумм от 1 до {m} 1/(i+j**2) равна: {mth.calc7(n, m):.4f}')
