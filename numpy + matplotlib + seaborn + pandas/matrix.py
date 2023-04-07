import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

i = 50
j = -50

#создаем и заполняем матрицу low - от этого число, high - до этого числа, size - размер двумерного массива
matrix = np.random.uniform(low=-50, high=50, size=(10,10))
#создаем тепловую карту. написать про цвета
sns.heatmap(matrix, annot = True, fmt='.1g',  vmin=-50, vmax=50, center= 0)
#показываем тепловую карту
plt.show()

#делаем из матрицы массив
a = matrix.flatten()

print (a)

sns.distplot(a, hist=True, kde=False, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'})

plt.show()