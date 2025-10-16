request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False}
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)


from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name = 'Мария', age=20, wieght=49, eyes_color='brown')
pprint(my_dict)


input_string = 'HelloWorld'
result = tuple(input_string)
print(result)
print(list(result))


def personal_info(name, age, company = 'unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")


tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)


def tuple_sort(*tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort(5, 5, 3, 1, 9))
    print(tuple_sort(5, 5, 2.1, '1', 9))




nums = input('Введите числа через пробел ')
nums_list = nums.split()
nums_list = [int(num) for num in nums_list]
nums_tuple = tuple(nums_list)
print(nums_list)
print(nums_tuple)


def remove_elem(date, elem):
    list_elem = list(date)
    if elem in list_elem:
        list_elem.remove(elem)
    return tuple(list_elem)

print(remove_elem((1, 2, 3), 1))
print(remove_elem((1, 2, 3, 1, 2, 3, 4, 5, 2, 4, 2), 3))
print(remove_elem((2, 4, 6, 6, 4, 2), 9))


def numpad_top(string):
    count = {}
    for char in string:
        num = int(char)
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    temp = []
    for num, elem in count.items():
        temp.append((elem, num))
    temp.sort(reverse=True)
    top = {}
    for i in range(3):
        if i < len(temp):
            elem, num = temp[i]
            top[num] = elem
    return dict(sorted(top.items()))

if __name__ == '__main__':
    print(numpad_top("638574583541365"))
    print(numpad_top("638574582368143"))


def id_start_end(id, elem):
    if elem not in id:
        return()
    start_id = id.index(elem)
    if id.count(elem) == 1:
        return id[start_id:]
    end_id = id.index(elem, start_id + 1)
    return id[start_id:end_id +1]

print(id_start_end((1, 2, 3), 8))
print(id_start_end((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(id_start_end((1, 2, 8, 5, 1, 2, 9), 8))


def sum_nums(nums):
    return sum(nums)

print(sum_nums([1, 2, 3]))
print(sum_nums([99, 23, 44]))
print(sum_nums([10, 20, 30, 40]))
