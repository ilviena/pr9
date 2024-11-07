import random
while True:
    try:
        n = int(input("Введите размерность списка: "))
        if n <= 0:
            print("Пожалуйста, введите положительное целое число!")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите целое число!")
list = [random.randint(-50, 50) for i in range(n)]
print(f"Сгенерированный список: {list}")
max_value = max(list)
min_value = min(list)
if max_value != min_value:
    for i in range(len(list)):
        if list[i] == max_value:
            list[i] = min_value
        elif list[i] == min_value:
            list[i] = max_value
    print(f"Список, в котором минимальный и максимальный элемент поменялись местами: {list}")
else:
    print("В списке все значения одинаковые")