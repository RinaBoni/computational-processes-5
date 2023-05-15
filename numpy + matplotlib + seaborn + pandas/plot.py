#построить график любой сложной функции. построить график этой же функции с добавлением шума

__author__ ="Borisova Ekaterina IVT20"


import matplotlib.pyplot as plt
import numpy as np
import math

plt.title('тройные углы')
plt.xlabel('x')
plt.ylabel('y')


#возвращает одномерный массив с равномерно разнесенными значениями внутри заданного интервала от 0 до 5 с шагом 0.01
x = np.arange(0,5,0.01)

#x и у являются массивами, а операции над ними векторными
#тройной угол (sin3a)
y =  3*np.sin(x**2)- 4*np.sin(x)**3
#шум (от -0.3 до 0.3, количество 500(то же количество точек что и в x))
y1 = y + np.random.uniform(-0.3,0.3,500)
#добавление тройного угла (sin3a), 'b'- синий цвет, label='sin3a'- название графика
plt.plot(x, y, 'b', label = 'sin3a')
#добавление шума, label = 'noise'sin3a- название графика, alpha = 0.3 - прозрачность графика
plt.plot(x, y1, label = 'noise sin3a', alpha = 0.3)


#тройной угол (cos3a)
z = 4*np.cos(x)**3 - 3*np.cos(x**2)
#шум (от -0.3 до 0.3, количество 500(то же количество точек что и в x))
z1 = z + np.random.uniform(-0.3,0.3,500)
#добавление тройного угла (cos3a), 'r'- красный цвет, label='cos3a'- название графика
plt.plot( x,z,'r', label='cos3a')
#добавление шума, label = 'noise cos3a'- название графика, alpha = 0.3 - прозрачность графика
plt.plot(x, z1, label = 'noise cos3a', alpha = 0.3)


#вывод легенды, loc='upper left' фиксация легенды в верхнем правом углу
plt.legend(loc='upper left')
#вывод координатной сетки
plt.grid(True)
#вывод графиков
plt.show()


