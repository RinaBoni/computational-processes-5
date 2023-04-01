import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

i = 50
j = -50

#создаем и заполняем матрицу
matrix = np.random.uniform(low=-1, high=1, size=(10,10))
#создаем тепловую карту
sns.heatmap(matrix, annot = True, fmt='.1g',  vmin=-1, vmax=1, center= 0)
#показываем тепловую карту
plt.show()

#матрицу в массив
a = matrix.flatten()
#создаем гистограму 
sns.distplot(a, hist=True, kde=False, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'})
#показываем гистограму (покажется после закрытия тепловой карты)
plt.show()