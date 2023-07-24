# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

min_n=int(input('Введите минимальное число: '))
max_n=int(input('Введите максимальное число: '))

list1=[random.randint(-10,20) for i in range(random.randint(1,20))]
print(list1)
list2=list()
for i in range(len(list1)):
    if list1[i]>=min_n and list1[i]<=max_n:
        list2.append(i)
print(list2)