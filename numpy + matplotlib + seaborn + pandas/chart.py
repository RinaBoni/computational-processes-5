import matplotlib.pyplot as plt
import numpy as np
import math

plt.title('тройные углы')
plt.xlabel('x')
plt.ylabel('y')

#возвращает одномерный массив с равномерно разнесенными значениями внутри заданного интервала
x = np.arange(-3, 4*np.pi, 0.5)
#тройной угол (sin3a)
y1 =  3*np.sin(x)- 4*np.sin(x)**3
#тройной угол (cos3a)
y2 = 4*np.cos(x)**3 - 3*np.cos(x)
 
plt.plot(x,y1,':b', label='sin3a')
plt.plot( x,y2,'red', label='cos3a')

plt.legend(fontsize=14, loc='upper left')
plt.tight_layout()
plt.show()


plt.plot(x,y1,':b', label='sin3a')
plt.plot( x,y2,'red', label='cos3a')
plt.scatter(x, y1, 'blue')
plt.scatter(x, y2, 'red')
plt.legend(fontsize=14, loc='upper left')
plt.tight_layout()
plt.show()
