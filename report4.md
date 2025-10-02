# Тема 4. Функции и стандартные модули/библиотеки 
Отчет по Теме 4 выполнил(а):
* Макарова Мария Александровна 
* ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
* Ротенштрайх Т. В.

# Лабораторная работа
## Задание №1

```python
def main():
    print(2+2)

if __name__ == '__main__':
    main()
```

# Результат
<img width="459" height="542" alt="image" src="https://github.com/user-attachments/assets/b9a7251c-e069-488c-b67e-8f07cfbf3c1a" />

# Вывод


## Задание №2

```python
def main():
    return 2+2
    
if __name__ == '__main__':
    print(main())
```

# Результат
<img width="459" height="542" alt="image" src="https://github.com/user-attachments/assets/697f835b-cdcb-421a-aa79-6c2f4b9f8bcd" />

# Вывод
Делает то же самое, но вместо print используем return.

## Задание №3

```python
def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)
```

# Результат
<img width="516" height="743" alt="image" src="https://github.com/user-attachments/assets/9091adce-ac3b-4bc3-b587-ba29f11aafc5" />

# Вывод


## Задание №4

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"onr={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")
```

# Результат 
<img width="747" height="752" alt="image" src="https://github.com/user-attachments/assets/ffb5903b-f946-4d7e-a343-4e600c657476" />

# Вывод

## Задание №5
```python
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
```

# Результат
<img width="928" height="1080" alt="image" src="https://github.com/user-attachments/assets/f0b8d706-c21c-4a23-a7d1-58af5dfc25f6" />

# Вывод

## Задание №6

```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])
```

# Результат
<img width="583" height="663" alt="image" src="https://github.com/user-attachments/assets/5ac0721d-0b4b-4c8a-add5-5b702b0e81b0" />

# Вывод

## Задание №7

```python
#for_import
def say_hello():
    print('Hello teacher!')

#main
from for_import import say_hello
if __name__ == '__main__':
    say_hello()
```

# Результат
<img width="583" height="449" alt="image" src="https://github.com/user-attachments/assets/33af9de1-0546-4e5c-a911-bed2a9065ac4" />

# Вывод

## Задание №8
```python
import math
def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()
```

# Результат
<img width="627" height="709" alt="image" src="https://github.com/user-attachments/assets/72ebe704-fb22-4f40-aba9-bb233668c0e1" />

# Вывод

## Задание №9
```python
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
```

# Результат
<img width="696" height="969" alt="image" src="https://github.com/user-attachments/assets/3d5d9b48-521d-4b2b-8554-3a6c0f91ae84" />

# Вывод

## Задание №10

```python
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
    result = 0,5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```

# Результат
<img width="698" height="1080" alt="image" src="https://github.com/user-attachments/assets/858ff581-aa3d-473f-81f7-0295f3a528ea" />

# Вывод

# Самостоятельная работа
## Задание №1

```python
```

# Результат

# Вывод

## Задание №2
```python
```

# Результат

# Вывод

## Задание №3
```python
```

# Результат

# Вывод

## Задание №4
```python
```

# Результат

# Вывод

## Задание №5
```python
```

# Результат

 
# Вывод

# Общий вывод
