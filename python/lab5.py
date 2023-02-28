#https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#Даны натуральное число n, действительные числа a1,..., an. Вычислить: д) a1^2 + ... + an^2;

__author__ ="Borisova Ekaterina IVT20"

num = []

n =int(input ("Введите количество элементов в массиве: "))

for i in range(n):
    num.append(float(input(f"Введите {i+1}-е число: ")))
    
sum = 0

for i in range(n):
    sum = sum + num[i]**2

print(f"Сумма равна: {sum}")