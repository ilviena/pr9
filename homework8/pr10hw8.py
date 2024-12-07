import random

def generate_ticket():
    """Генерирует лотерейный билет."""
    return [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
def user_selection(ticket):
    """Запрашивает у пользователя выбор чисел из каждой строки."""
    user_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} ({ticket[i]}): "))
                if number in ticket[i]:
                    user_numbers.append(number)
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите число из предложенного списка.")
            except ValueError:
                print("Пожалуйста, введите целое число.")
    return user_numbers
def random_selection(ticket):
    """Случайный выбор чисел из каждой строки."""
    return [random.choice(row) for row in ticket]
def check_matches(user_numbers, random_numbers):
    """Проверяет совпадения между числами пользователя и случайными числами."""
    matches = set(user_numbers) & set(random_numbers)
    return matches
def main():
    ticket = generate_ticket()
    print("Добро пожаловать в лотерею!")
    user_numbers = user_selection(ticket)
    random_numbers = random_selection(ticket)
    print(f"\nВаши числа: {user_numbers}")
    print(f"Случайно выбранные числа: {random_numbers}")
    matches = check_matches(user_numbers, random_numbers)
    if matches:
        print(f"\nПоздравляем! Вы угадали следующие числа: {matches}")
    else:
        print("\nК сожалению, у вас нет совпадений.")
if __name__ == "__main__":
    main()
