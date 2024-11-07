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
s = []
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        s.append(list[i])
if s:
    print(f"Все элементы списка, которые больше предыдущего элемента: {s}")
else:
    print("Нет элементов списка, которые больше предыдущего")