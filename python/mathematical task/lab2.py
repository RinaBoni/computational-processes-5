#https://ivtipm.github.io/Programming/Glava02/index02.htm#z43
#Даны три действительных числа. 
#Возвести в квадрат те из них, значения которых неотрицательны.

__author__ ='Borisova Ekaterina IVT20'

num = []

n = 3

for i in range(n):
    num.append(float(input(f"Введите {i+1}-е число: ")))
    

for i in range(n):
    if num[i] > 0:
        num[i] = num[i]**2
        print(f"{i+1}-е число изменено: {num[i]}")