# Тема 7. Работа с файлами (ввод, вывод).
Отчет по Теме #7 выполнил(а):
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
Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
```python
код не предусмотрен
```

# Результат
<img width="326" height="457" alt="image" src="https://github.com/user-attachments/assets/d3ac1037-61f2-4f43-aced-490e6a6856da" />

# Вывод
Создали текстовый файл в python. 

## Задание №2
Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

# Результат
<img width="383" height="419" alt="image" src="https://github.com/user-attachments/assets/3149b422-15cc-4bad-ac5f-f345e3513687" />

# Вывод
С помощью функции open() открыли текстовый файл, а с помощью readline() прочитали первую строку текстрового файла, после чего закрыли файл с помощью f.close(). 

## Задание №3
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

# Результат
<img width="469" height="385" alt="image" src="https://github.com/user-attachments/assets/153b0dd1-a740-4648-a28c-b4c333bc0410" />

# Вывод
С помощью функции open() открыли текстовый файл, а с помощью readlines() прочитали первую строку текстрового файла, после чего закрыли файл с помощью f.close().

## Задание №4
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```

# Результат 
<img width="450" height="420" alt="image" src="https://github.com/user-attachments/assets/a019997e-89b9-4963-aa55-332c563c1b47" />

# Вывод
Используя конструкцию with open() и функцию readlines() вывели все строки кода в виде массива. 

## Задание №5
Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

# Результат
<img width="399" height="482" alt="image" src="https://github.com/user-attachments/assets/ce02d510-b043-40c8-a586-e78757be724d" />

# Вывод
Используя конструкцию with open() и цикл for, вывели каждую строку из текстового файла. 

## Задание №6
Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

# Результат
<img width="648" height="510" alt="image" src="https://github.com/user-attachments/assets/5182693f-f6aa-4162-8cc2-c28277b9f0c7" />
<img width="647" height="449" alt="image" src="https://github.com/user-attachments/assets/fcbc5a00-2cc0-48aa-bec4-bfbfa4afe32b" />

# Вывод
Используя конструкцию with open() с режимом 'a+', добавили новую строку в файл, а затем прочитали и вывели все строки из файла.

## Задание №7
Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

# Результат
<img width="479" height="488" alt="image" src="https://github.com/user-attachments/assets/1960d968-378b-4161-83c6-c397a6f03275" />
<img width="479" height="442" alt="image" src="https://github.com/user-attachments/assets/41c8dc0d-e82e-4266-a26f-74d88effec8b" />

# Вывод
Используя цикл for, записали в файл три строки с текстом "Cycle run" и содержимым списка, а в конце вывели слово "Done!".

## Задание №8
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[1]])}')
    print('-' * 48)

print_docs('C:/Users/User/OneDrive/Desktop/работы/учеба/ПИ/Тема 7')
```

# Результат
<img width="754" height="689" alt="image" src="https://github.com/user-attachments/assets/3e47429b-97f8-4fbf-94af-b4ede298f6c0" />

# Вывод
Создали функцию print_docs(), которая с помощью функции os.walk() проходит по всем папкам указанной директории, а затем для каждой папки выводит список содержащихся в ней подпапок и файлов с помощью функций print() и join().

## Задание №9
Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.
```python
def longest_words(file):
    with open(file, encoding = 'utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key = len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

# Результат
<img width="553" height="644" alt="image" src="https://github.com/user-attachments/assets/756541ee-a758-4b1c-9220-fa1ad85a975c" />

# Вывод
Создали функцию longest_words(), которая с помощью функции open() открывает файл, затем функциями read() и split() читает весь текст и разбивает его на слова. Функция max() с параметром key=len находит максимальную длину слова, а цикл for с функцией len() собирает все слова этой длины. В конце функция возвращает одно слово или список самых длинных слов, которые выводятся с помощью print().

## Задание №10
Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
* № - номер по порядку (от 1 до 300); Михаил А. Панов
* Секунда – текущая секунда на вашем ПК;
* Микросекунда – текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding = 'utf-8', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

# Результат
<img width="738" height="604" alt="image" src="https://github.com/user-attachments/assets/acc5bb89-3676-4547-8db4-a50421ead93a" />
<img width="538" height="1080" alt="image" src="https://github.com/user-attachments/assets/4f39973e-23c9-48b4-98a6-be9a18f62d5d" />

# Вывод
Создали CSV-файл с помощью модуля csv, используя функцию writer() для записи данных. Функция writerow() записывает заголовки и 300 строк с номером, текущей секундой и микросекундой, которые получаются с помощью datetime.datetime.now(). Функция time.sleep() добавляет задержку между записями строк.

# Самостоятельная работа
## Задание №1
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
with open("article.txt", "r", encoding = 'utf-8') as f:
    text = f.read()
words = text.split()
word_count = len(words)
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
max_word = ""
max_count = 0
for word, count in word_freq.items():
    if count > max_count:
        max_count = count
        max_word = word
print(f"Всего слов: {word_count}")
print(f"Самое частое слово: '{max_word}' встречается {max_count} раз")
```

# Результат
<img width="1920" height="323" alt="image" src="https://github.com/user-attachments/assets/87413672-aaaa-442e-b5c1-9a8b00aebcc6" />
<img width="736" height="823" alt="image" src="https://github.com/user-attachments/assets/8ef36dfe-2162-405d-b2ec-da733a48d4a6" />

# Вывод
Открыли файл с помощью функции open() и прочитали весь текст функцией read(). Разбили текст на слова с помощью split() и посчитали их количество функцией len(). Создали словарь частот слов, используя метод get() для подсчета. С помощью цикла for и метода items() нашли самое частое слово, которое вывели вместе с общим количеством слов функцией print().

## Задание №2
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
def main():
    while True:
        print("Ввести информацию о расходах - 1")
        print("Вывести информацию - 2")
        print("Выйти - 3")
        choice = input("Выберите действие: ")
        if choice == "1":
            category = input("Категория расхода: ")
            amount = input("Сумма расхода: ")
            description = input("Описание: ")
            with open("expenses.txt", "a", encoding="utf-8") as f:
                f.write(f"{category} | {amount} | {description}\n")
            print("Расход добавлен!")
        elif choice == "2":
            with open("expenses.txt", "r", encoding="utf-8") as f:
                expenses  = f.read()
                print(expenses)
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
```

# Результат
<img width="712" height="1058" alt="image" src="https://github.com/user-attachments/assets/2da1e962-96b7-4606-945b-9e2bed3b57e8" />
<img width="713" height="621" alt="image" src="https://github.com/user-attachments/assets/14cdbead-194b-417e-bf54-cec99f265324" />

# Вывод
Создали функцию main(), которая с помощью цикла while True и функций print() выводит меню управления. Функция input() принимает выбор пользователя, а затем в зависимости от выбора: записывает данные в файл с помощью open() и write(), читает и выводит данные с помощью read(), или завершает программу с помощью break.

## Задание №3
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
* Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
* Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines
```python
with open("input.txt", "r", encoding= 'UTF-8') as f:
    content = f.read()

lines = content.split('\n')
num_lines = len(lines)

words = content.split()
num_words = len(words)

letters = 0
for char in content:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letters += 1

print(f"В тексте {letters} букв, {num_words} слов, {num_lines} строк")
```

# Результат
<img width="734" height="709" alt="image" src="https://github.com/user-attachments/assets/ffc587e0-9eab-4baf-9380-e3763826d7fa" />

# Вывод
Открыли файл с помощью функции open() и прочитали весь текст функцией read(). Разбили текст на строки и слова с помощью split(), посчитали их количество функцией len(). С помощью цикла for и проверки символов посчитали количество букв латинского алфавита. Вывели всю статистику с помощью функции print().

## Задание №4
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
* Запрещенные слова: hello email python the exam wor is
* Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
* Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!
```python
with open("input.txt", "r", encoding='UTF-8') as f:
    banned_words = f.read().split()

sentence = input("Введите предложение: ")

result = sentence
for word in banned_words:
    start = 0
    while True:
        index = result.lower().find(word, start)
        if index == -1:
            break

        stars = '*' * len(word)
        result = result[:index] + stars + result[index + len(word):]
        start = index + len(stars)

print("\nРезультат:")
print(result)
```

# Результат
<img width="1113" height="834" alt="image" src="https://github.com/user-attachments/assets/9b7df45b-0d6f-4c0c-a6b3-5747a63c8e7f" />

# Вывод
Открыли файл с помощью функции open(), прочитали запрещенные слова функцией read() и разбили их на список с помощью split(). Функция input() получила предложение от пользователя. С помощью цикла for и метода find() в нижнем регистре (lower()) нашли все запрещенные слова, которые заменили на звездочки с помощью умножения строки. Результат вывели функцией print().

## Задание №5
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
```python
with open("input.txt", "r", encoding= 'UTF-8') as f:
    content = f.read()

words = content.split()
num_words = len(words)

print(f"В тексте {num_words} слов")
```

# Результат
<img width="588" height="531" alt="image" src="https://github.com/user-attachments/assets/b94fda8a-08fe-4048-850a-660a63e323fe" />
<img width="458" height="1014" alt="image" src="https://github.com/user-attachments/assets/a1e3d832-acaa-43fd-a675-d7007038db3b" />

# Вывод
Открыли файл с помощью функции open() и прочитали весь текст функцией read(). Разбили текст на слова с помощью split() и посчитали их количество функцией len(). Вывели результат с помощью функции print().

# Общий вывод
Во время выполнения данных лабораторной и самостоятельной работ с файлами, вводом и выводом мы использовали различные встроенные функции: open() для открытия файлов, read() и readlines() для чтения, write() для записи, split() для разделения текста, len() для подсчета элементов, find() и lower() для поиска и обработки текста, а также input() для ввода данных и print() для вывода результатов. Для специальных задач применяли datetime.now() и time.sleep() для работы со временем, get() и items() для словарей, max() с параметром key для поиска максимальных значений.
