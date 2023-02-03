# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите цифру дня недели: '))
if a <= 5:
    print("нет")
else:
    print("да")

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату по оси X: '))
y = int(input('Введите координату по оси Y: '))
if x > 0 and y > 0:
    print('Точка находится в 1й четверти.')
elif x < 0 and y > 0:
    print('Точка находится во 2й четверти.')
elif x < 0 and y < 0:
    print('Точка находится в 3й четверти.')
elif x > 0 and y < 0:
    print('Точка находится в 4й четверти.')
elif x == 0 or y == 0:
    print('При поиске четверти, координаты не могут быть равны нулю.')


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
number = int(input('Введите номер четверти: '))
if number == 1:
    print('Диапазон точек: x > 0 and y > 0')
elif number == 2:
    print('Диапазон точек: x < 0 and y > 0')
elif number == 3:
    print('Диапазон точек: x < 0 and y < 0')
elif number == 4:
    print('Диапазон точек: x > 0 and y < 0')
elif number < 0 or number > 4:
    print('Введите верную четверть')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = int(input('Введите координату A по оси X: '))
ay = int(input('Введите координату A по оси Y: '))
bx = int(input('Введите координату B по оси X: '))
by = int(input('Введите координату B по оси Y: '))
distance = (((bx - ax)**2 + (by - ay)**2))**0.5
print(round(distance, 2))