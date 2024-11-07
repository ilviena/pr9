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
even_count = 0
odd_count = 0
another_count = 0
for i in s:
    if float(i)%2 == 0:
        even_count += 1
    elif float(i)%2 == 1:
        odd_count += 1
    else:
        another_count += 1
print(f"Количество четных чисел - {even_count}, нечетных чисел - {odd_count}")
print(f"Количество ни четных, ни нечетных чисел (нецелых) - {another_count}")