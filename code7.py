f = open('input.txt', 'r')
print(f.readline())
f.close()


f = open('input.txt', 'r')
print(f.readlines())
f.close()


with open('input.txt') as f:
    print(f.readlines())


with open('input.txt') as f:
    for line in f:
        print(line)


with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)



lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')



import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[1]])}')
    print('-' * 48)

print_docs('C:/Users/User/OneDrive/Desktop/работы/учеба/ПИ/Тема 7')



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



with open("input.txt", "r", encoding= 'UTF-8') as f:
    content = f.read()

words = content.split()
num_words = len(words)

print(f"В тексте {num_words} слов")
