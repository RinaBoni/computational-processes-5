import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

i = 50
j = -50

#создаем и заполняем матрицу
matrix = np.random.uniform(low=-50, high=50, size=(10,10))
#создаем тепловую карту
sns.heatmap(matrix, annot = True, fmt='.3g',  vmin=-50, vmax=50, center= 0)
#показываем тепловую карту
plt.show()

a = matrix.flatten()

print (a)

sns.distplot(a, hist=True, kde=False, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'})

plt.show()