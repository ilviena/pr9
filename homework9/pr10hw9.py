import re

def split_email(email):
    pattern = r'^(?P<username>[^@]+)@(?P<domain>.+)$'
    match = re.match(pattern, email)
    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        raise ValueError("Неверный формат email.")

def main():
    email = input("Введите ваш email: ")
    
    try:
        username, domain = split_email(email)
        print(f"Имя пользователя: {username}")
        print(f"Доменное имя: {domain}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
