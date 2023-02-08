# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

spisok = [2, 3, 4, 5, 6]
new_spisok = []
count = len(spisok)
for i in range(len(spisok)):
    while i < len(spisok)/2 and count > len(spisok)/2:
        count -= 1
        new_spisok.append(spisok[i] * spisok[count])
        i += 1
print(new_spisok)
