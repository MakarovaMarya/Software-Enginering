def main():
    print(2+2)

if __name__ == '__main__':
    main()



def main():
    return 2+2
    
if __name__ == '__main__':
    print(main())



def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)



def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"onr={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")



def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    print()
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()
    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})



def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])



#for_import
def say_hello():
    print('Hello teacher!')

#main
from for_import import say_hello
if __name__ == '__main__':
    say_hello()



import math
def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()



from datetime import datetime as dt
from datetime import timedelta as td
def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()



global result
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")



from datetime import datetime  # Импортируем класс datetime из модуля datetime для работы с датой и временем
from math import sqrt  # Импортируем функцию sqrt из модуля math для вычисления квадратного корня

def main(**kwargs):  # Определяем главную функцию, которая принимает произвольное количество именованных аргументов
    for key in kwargs.items():  # Итерируемся по всем элементам словаря kwargs (возвращает пары ключ-значение)
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)  # Вычисляем длину вектора по теореме Пифагора для текущего значения (списка из двух чисел)
        print(result)  # Выводим полученный результат на экран

if __name__ == '__main__':  # Проверяем, запущен ли скрипт напрямую (а не импортирован как модуль)
    start_time = datetime.now()  # Засекаем время начала выполнения программы
    main(  # Вызываем функцию main с передачей именованных аргументов
        one=[10, 3],     # Аргумент one со списком [10, 3]
        two=[5, 4],      # Аргумент two со списком [5, 4]
        three=[15, 13],  # Аргумент three со списком [15, 13]
        four=[93, 53],   # Аргумент four со списком [93, 53]
        five=[133, 15]   # Аргумент five со списком [133, 15]
    )
    time_costs = datetime.now() - start_time  # Вычисляем разницу между текущим временем и временем начала (продолжительность выполнения)
    print(f"Время выполнения программы - {time_costs}")  # Выводим время выполнения программы в формате строки



import random

def play():
    value = random.randint(1, 6)
    print(f"Выпало число: {value}")
    if value in [5, 6]:
        print(f"Вы победили")
    elif value in [3, 4]:
        play()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    play()



import datetime
import time

for i in range(5):
    current_time = datetime.datetime.now()
    print("Текущее время:",str(current_time)[:19])
    time.sleep(1)



def var(*args):
    print(sum(args) / float(len(args)))

if __name__ == '__main__':
    var(47, 23, 89, 12, 65, 34, 91, 5, 78)



#Heron
import math
def fun_Heron(a, b, c):
    p = (a + b + c) / 2
    val = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return val

#main
from Heron import fun_Heron

def main():
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    area = fun_Heron(a, b, c)
    print(f"Площадь треугольника: {area:,.2f} см²")

if __name__ == '__main__':
    main()
