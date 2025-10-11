set_1 = {'White', 'Black', 'Red', 'Pink'}
set_2 = {'Red', 'Green', 'Blue', 'Red'}

print(set_1 - set_2)


#вариант с set()
a = set('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)

#вариант с frozenset()
a = frozenset('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)


def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory

    return input_list

print(replace([1, 2, 3, 4, 5]))


a = [12, 54, 32, 57, 843, 2346, 765, 75, 25, 234, 756, 23]
print(a[2:6])


def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 3, 33]))
print(useless([-12.5, 54, 77.3, 0, -36, 98.2, -63, 21.7, 47, -89.6]))
print(useless([-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]))


superheroes = ['superman', 'spiderman', 'batman']

nikolay, vasiliy, ivan = superheroes

print('Николай - ', nikolay)
print('Василий - ', vasiliy)
print('Иван - ', ivan)


a = [-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]
a.sort()
print('Отсортированный список:\n', a)
a.pop(0)
print('Отсортированный список без наименьшего элемента:\n', a)


from random import randint

def list_maker():
    a = [randint(1, 100)] * randint(3, 10)
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1, 5)):
        result.append(list_maker())
    print(result)


def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print(f'Супермножество не обнаружено')

if __name__ == '__main__':
    superset({1, 8, 3, 5}, {3, 5})
    superset({1, 8, 3, 5}, {5, 3, 8, 1})
    superset({3, 5}, {5, 3, 8, 1})
    superset({90, 100}, {3, 5})


my_list = [2, 5, 8, 3]
print(my_list[::-1])



list_check = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201,
              8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998,
              1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778,
              8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016,
              4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250,
              7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777,
              9865, 5678, 8201, 4445, 3016, 4506, 4506]

print(f"Было выдано {len(list_check)} чеков")
print(f"Ресторан посетило {len(set(list_check))} разных людей")
count = 0
for i in list_check:
    current_count = list_check.count(i)
    if current_count > count:
        count = current_count
        digit = i
print(f"Больше всех раз ресторан посетил работник {digit}")


list_result = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
list_sort = sorted(list_result)
print(f"Три лучших результата бега: {list_sort[0], list_sort[1],list_sort[2]}")
print(f"Три худших результата бега: {list_sort[-3], list_sort[-2],list_sort[-1]}")
print(f"Все результаты начиная с десятого: {list_result[9:]}")


from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def s_triangle(a, b, c):
    p = (a + b + c) / 2.0
    result = sqrt(p * (p - a) * (p - b) * (p - c))
    return result

if __name__ == '__main__':
    print(f"Площадь треугольника с максимальными сторонами: {s_triangle(max(one), max(two), max(three)):.2f}")
    print(f"Площадь треугольника с минимальными сторонами: {s_triangle(min(one), min(two), min(three))}")


student1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
student2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
student3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

student1 = [4 if x == 3 else x for x in student1 if x != 2]
student2 = [4 if x == 3 else x for x in student2 if x != 2]
student3 = [4 if x == 3 else x for x in student3 if x != 2]

print(student1)
print(student2)
print(student3)


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def create_set(lst):
    result = set()
    for num in set(lst):
        count = lst.count(num)
        result.add(num)
        for repeat in range(2, count + 1):
            result.add(str(num) * repeat)
    return result

set_1 = create_set(list_1)
set_2 = create_set(list_2)
set_3 = create_set(list_3)

print(set_1)
print(set_2)
print(set_3)
