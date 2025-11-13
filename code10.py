from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(100))


def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = "Недопустимый возраст"
        input_func(name, age)
    return output_func

@check
def personal_info(name, age):
    print(f"Имя: {name} Возраст: {age}")

if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Александр', -5)
    personal_info('Петр', 138, 15, 48, 2)


def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1, 15, 'Hello', 'i', 'try', 'to', 'crash', 'your', 'site', 38, 45])


class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678910'
    check_name(name)


class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного включения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')




import time

def is_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения программы {func.__name__} составляет {execution_time}")
        return result
    return wrapper

@is_time
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()


def file_reader(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print(content)
    except Exception as ex:
        print(ex)

print("Проверка содержимого файлов")
file_reader("empty_file.txt")
file_reader("file_with_text.txt")


def sum_of_num():
    try:
        user_input = input("Введите число: ")
        num = float(user_input)
        result = 2 + num
        print(f"Результат: {result}")
        return result
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    sum_of_num()
    sum_of_num()
    sum_of_num()


class MyDecorator:
    def __init__(self, operation_name):
        # Сохраняем название операции для красивого вывода
        self.operation_name = operation_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Выводим информацию о начале операции и входных данных
            print(f"-- Начало операции: {self.operation_name}")
            print(f"   Входные данные: {args}")

            # Вызываем оригинальную функцию и сохраняем результат
            result = func(*args, **kwargs)

            # Выводим результат выполнения операции
            print(f"   Результат: {result}")
            print(f"-- Конец операции: {self.operation_name}")
            print("-" * 50)  # Разделитель для читаемости

            return result  # Возвращаем результат оригинальной функции

        return wrapper  # Возвращаем обернутую функцию


# Первая функция - сложение произвольного количества чисел
@MyDecorator("Сложение чисел")  # Применяем декоратор с названием операции
def add_nums(*nums):
    return sum(nums)


# Вторая функция - умножение произвольного количества чисел
@MyDecorator("Умножение чисел")  # Другой декоратор с другим названием
def multiply_nums(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


# Тестируем наши функции с декораторами
if __name__ == '__main__':
    print("Запуск программы с математическими операциями")
    print("=" * 50)

    # Тестируем сложение с разным количеством аргументов
    add_nums(1, 2, 3)  # 1 + 2 + 3 = 6
    add_nums(10, 20, 30, 40)  # 10 + 20 + 30 + 40 = 100
    add_nums(5)  # 5 = 5
    add_nums(2, 4, 6, 8, 10)  # 2 + 4 + 6 + 8 + 10 = 30

    # Тестируем умножение с разным количеством аргументов
    multiply_nums(2, 3, 4)  # 2 × 3 × 4 = 24
    multiply_nums(1, 2, 3, 4, 5)  # 1 × 2 × 3 × 4 × 5 = 120
    multiply_nums(10)  # 10 = 10
    multiply_nums(2, 5)  # 2 × 5 = 10
    multiply_nums(3, 3, 3)  # 3 × 3 × 3 = 27

    print("Все операции завершены!")


class InvalidEmailError(Exception):
    def __init__(self, email, reason=""):
        self.email = email
        self.reason = reason
        super().__init__(f"Некорректный email адрес: '{email}'. Причина: {reason}")


class UserRegistration:
    @staticmethod
    def validate_email(email):
        if not email:
            raise InvalidEmailError(email, "email не может быть пустым")
        if '@' not in email:
            raise InvalidEmailError(email, "отсутствует символ @")
        parts = email.split('@')
        if len(parts) != 2:
            raise InvalidEmailError(email, "неправильный формат email")
        local_part, domain = parts
        if not local_part:
            raise InvalidEmailError(email, "локальная часть (до @) не может быть пустой")
        if not domain:
            raise InvalidEmailError(email, "доменная часть (после @) не может быть пустой")
        if '.' not in domain:
            raise InvalidEmailError(email, "доменная часть должна содержать точку")
        # Дополнительная проверка на пробелы
        if ' ' in email:
            raise InvalidEmailError(email, "email не может содержать пробелы")
        return True

    def register_user(self, username, email):
        print(f"Попытка регистрации пользователя: {username}")
        print(f"   Email: {email}")
        try:
            self.validate_email(email)
            print(f"Пользователь {username} успешно зарегистрирован!")
            return True
        except InvalidEmailError as ex:
            print(f"Ошибка регистрации: {ex}")
            return False

if __name__ == '__main__':
    print("Проверка работы исключений InvalidEmailError")
    # Создаем экземпляры классов
    registration_system = UserRegistration()

    # Успешные регистрации
    registration_system.register_user("Иван Иванов", "ivan@example.com")
    print()

    # Регистрации с ошибками (вызовут наше исключение)
    registration_system.register_user("Ошибка1", "без-собаки.com")
    print()
    registration_system.register_user("Ошибка2", "пробел @example.com")
    print()
    registration_system.register_user("Ошибка3", "")
    print()
    registration_system.register_user("Ошибка4", "толькодомен@")
    print()

    print("\nРабота завершена!")
