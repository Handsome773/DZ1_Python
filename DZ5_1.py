# # 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Вариант 1
text = str(input())
text = text.split()
result = []
for i in text:
    if 'абв' not in i:
        result.append(i)
print(result)