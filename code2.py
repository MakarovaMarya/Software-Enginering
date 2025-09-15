print(5)
print('15')
print(2.3)

print(516 - 125)
print(17.5 + 2.3)
print(5 + 12.2 + 2 + 2.2)

print('Привет, Мир!')
world = 'Мир'
print(f"Привет, {world}!")
one = 'Привет, '
two = 'Мир!'
print(one + two)

one = 12.8
print(bool(one))
two = 15.2
print(int(two))
three = None
print(str(three))

one = input('one:')
two = input('two:')
three = input('three:')
print(one, two, three)

a = 14
b = 3
print('Возведение в степень:', a ** b)
print('Обычное деление:', a / b)
print('Целочисленное деление:', a // b)
print('Нахождение остатка от деления:', a % b)

line = 'To'
print(line * 3)

count_o = 'Hello World'
print(count_o.count('o'))

print('Hello\nWorld')

line = 'Hello World '
print(line[1])
print(line[:5])

print(bool(0))

a, b, c = 1, 2, 3
print(a, b, c)

print(int(input()))

line = 'abcd'
print(line *6)

day, month, year = 15, 'января', 2025
print(f"Сегодня {day} {month} {year}.", end=' Всего хорошего!')

my = 'my'
print(f'Hello {my} World')

print(len('Hello World'))

line = 'HELLO WORLD'
print(line.lower())

num = int(input("Введите трехзначное число: "))
a = num // 100
b = num // 10 % 10
c = num % 10
sum_digits = a + b + c
product = a * b * c
print(f"Сумма цифр: {sum_digits}")
print(f"Произведение цифр: {product}")

surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")
patronymic = input("Введите ваше отчетство: ")
print("ФИО:", f"{surname} {name} {patronymic}")
