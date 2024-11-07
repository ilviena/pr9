def correct_input(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
s = []
while True:
    num = input('Введите число: ')
    if num == 'end':
        break
    if correct_input(num):
        s.append(num)
    else:
        print('Введено не число!')
s = [num for num in s if float(num)%2 == 1]
print(f"Все нечетные введенные числа: {s}")