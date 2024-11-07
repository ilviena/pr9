import random
while True:
    try:
        n = int(input("Введите размерность списка: "))
        if n <= 0 :
            print("Пожалуйста, введите положительное целое число!")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите целое число!")
list = [random.randint(-50, 50) for i in range(n)]
print(f"Сгенерированный список: {list}")
new_list = [list[-1]] + [list[i] for i in range(len(list)-1)]
print(f"Сдвинутый список: {new_list}")