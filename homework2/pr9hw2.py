def correct_input(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    if correct_input(a) and correct_input(b):
        break
    else:
        print('Неверный ввод!')

a = int(float(a))
b = int(float(b))
s = []

if a == b or abs(a - b) == 1:
    print('Между введенными числами нет целых чисел')
elif a < b:
    print('Квадраты целых чисел, расположенных между введенными числами:')
    for i in range(a + 1, b):
        s.append(i**2)
else:
    print('Квадраты целых чисел, расположенных между введенными числами:')
    for i in range(b + 1, a):
        s.append(i**2)
print(s)