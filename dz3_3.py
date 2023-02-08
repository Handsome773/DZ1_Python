# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []
for i in range(len(list)):
    new_list.append(list[i] % 1)
min_el = 1
max_el = 0
for i in new_list:
    if i < min_el and i != 0:
        min_el = i
for i in new_list:
    if i > max_el:
        max_el = i
print(int((max_el - min_el) * 100) / 100)