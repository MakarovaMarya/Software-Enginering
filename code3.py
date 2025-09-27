one = int(input("Введите значение первой переменной: "))
two = int(input("Введите значение второй переменной: "))
if one >= two:
    print("Выполняется")
else:
    print("Не выполняется")

one = int(input("Введите значение переменной: "))
if one < 0:
    print('Переменная меньше 0')
elif 0 < one < 10:
    print('Переменная больше 0 и меньше 10')
else:
    print('Переменная больше 10')

numbers = [1, 3, 4, 6, 8, 9]
value = int(input('Введите значение переменной: '))
if value in numbers:
    print('Переменная есть в данном массиве')
else:
    print('Переменной нет в данном массиве')

numbers = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
value = int(input('Введите значение переменной: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная четная и есть в массиве numbers')
    else:
        print('Переменная нечетная и есть в массиве numbers')
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")

for i in range(10):
    print('i = ', i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print('Переменная равна 2 или 3')
    elif i in [4, 5, 6]:
        print('Переменная равна 4, 5 или 6')
    else:
        break

  string = 'Привет всем изучающим Python!'
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")

value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)

value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)

value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)

even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четные')

num = 1
for i in range(2):
    num *= 5
    num += 1
print(num)

text = "Hello World"
for char in reversed(text):
    print(char)

num = int(input('Введите число в диапазоне от 0 до 10 включительно: '))
if 0 <= num <= 3:
    print('Это число из диапазона от 0 до 3 включительно')
elif 3 < num < 6:
    print('Это число из диапазона от 3 до 6')
elif 6 <= num <= 10:
    print('Это число из диапазона от 6 до 10 включительно')
else:
    print('Ваше число не подходит по требованиям!')

s = input("Введите предложение на английском: ")
print(f"Длина предложения: {len(s)}")
print(f"В нижнем регистре: {s.lower()}")
vowels = sum(1 for char in s.lower() if char in 'aeiou')
print(f"Количество гласных: {vowels}")
new_s = s.replace('ugly', 'beauty').replace('Ugly', 'Beauty')
print(f"После замены 'ugly' на 'beauty': {new_s}")
starts = s.startswith('The')
ends = s.endswith('end')
print(f"Начинается с 'The': {starts}")
print(f"Заканчивается на 'end': {ends}")

counter = 0
while counter != 10:
    string = 'hello'
    memory = ' world'
    values = [0, 2, 4, 6, 8, 10]
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1
if counter > 7:
    print(string + memory)
