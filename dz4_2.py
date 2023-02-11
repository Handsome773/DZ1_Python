# 2) Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
n = int(input('Введите число: '))
res_list = []
for i in range(2, n + 1):
    if n % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            res_list.append(i)
print(res_list)44