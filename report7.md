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

```python
код не предусмотрен
```

# Результат
<img width="326" height="457" alt="image" src="https://github.com/user-attachments/assets/d3ac1037-61f2-4f43-aced-490e6a6856da" />

# Вывод

## Задание №2

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

# Результат
<img width="383" height="419" alt="image" src="https://github.com/user-attachments/assets/3149b422-15cc-4bad-ac5f-f345e3513687" />

# Вывод

## Задание №3
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

# Результат
<img width="469" height="385" alt="image" src="https://github.com/user-attachments/assets/153b0dd1-a740-4648-a28c-b4c333bc0410" />

# Вывод

## Задание №4
```python
with open('input.txt') as f:
    print(f.readlines())
```

# Результат 
<img width="450" height="420" alt="image" src="https://github.com/user-attachments/assets/a019997e-89b9-4963-aa55-332c563c1b47" />

# Вывод

## Задание №5
```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

# Результат
<img width="399" height="482" alt="image" src="https://github.com/user-attachments/assets/ce02d510-b043-40c8-a586-e78757be724d" />

# Вывод

## Задание №6
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

## Задание №7
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

## Задание №8
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

## Задание №9
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

## Задание №10
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

# Самостоятельная работа
## Задание №1
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

## Задание №2
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
