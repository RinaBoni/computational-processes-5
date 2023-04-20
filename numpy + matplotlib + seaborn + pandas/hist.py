#создать случайную матрицу numpy array
#превратть матрицу в массив, построить гистограмму (seaborn)

__author__ ="Borisova Ekaterina IVT20"

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#создаем и заполняем матрицу low - от этого число, high - до этого числа, size - размер двумерного массива
matrix = np.random.randint(low=-50, high=50, size=(10,10))

#делаем из матрицы массив
a = matrix.flatten()

#создаем гисторгмму
sns.histplot(a)

plt.show()