# 1) Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.

a = float(input('Введите исходное число: '))
d = float(input('Введите "точность" вывода: '))
count = 0
if d == 1:
    print(int(a))
else:
    while d != 1:
        d *= 10
        count += 1
    print(round(a, count))