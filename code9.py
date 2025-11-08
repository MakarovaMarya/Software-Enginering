class Maria:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Мария':
            self.name = f"Да, Я {name}"
        else:
            self.name = f"Я не {name}, а Мария"

person1 = Maria('Света')
person2 = Maria('Мария')
print(person1.name)
print(person2.name)

person2.surname = 'Макарова'

class IceCream:
    def __init__(self, ingredient=None):
        self.base_price = 59
        if isinstance(ingredient, str):
            self.ingredient = ingredient
            self.price = self.base_price + 39
        else:
            self.ingredient = None
            self.price = self.base_price

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient} - {self.price} руб.")
        else:
            print(f"Обычное мороженое - {self.price} руб.")

icecream = IceCream()
icecream.composition()
icecream = IceCream('шоколадом')
icecream.composition()
icecream = IceCream(2)
icecream.composition()

class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):  # установка значения атрибута
        self._value = value

    def get_value(self):  # получение значения атрибута
        return self._value

    def del_value(self):  # удаление атрибута
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
# Ошибка возникает потому, что после вызова obj.del_value() атрибут _value
# был удален из объекта, и при попытке получить его значение через get_value()
# происходит обращение к несуществующему атрибуту, что вызывает ошибку AttributeError.

class Mammal:
    class_name = 'Млекопитающим'
    feeding_type = 'молоком'


class Dog(Mammal):
    species = 'собака'
    sounds = 'гав'
    special_ability = 'искать и приносить предметы'


class Cat(Mammal):
    species = 'кошка'
    sounds = 'мяу'
    special_ability = 'видеть в темноте'

dog = Dog()
cat = Cat()

print(f"Собака относится к {dog.class_name}, издает звук {dog.sounds}, питается {dog.feeding_type}, особое умение - {dog.special_ability}")
print(f"Кошка относится к {cat.class_name}, издает звук {cat.sounds}, питается {cat.feeding_type}, особое умение - {cat.special_ability}")

class Russian:
    @staticmethod
    def greeting():
        return "Привет"

class English:
    @staticmethod
    def greeting():
        return "Hello"

def print_greetings():
    languages = [(Russian, "русском"), (English, "английском")]
    for language, lang_name in languages:
        print(f"На {lang_name} языке говорят: {language.greeting()}")

print_greetings()




class Tomato:
    # Статические свойства - стадии созревания помидора
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        # _index - защищенное свойство (индекс томата)
        # _state - защищенное свойство (текущая стадия созревания)
        self._index = index
        self._state = 0  # Начинаем с первой стадии

    def grow(self):
        # Переводит томат на следующую стадию созревания
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        # Проверяет, созрел ли томат (достиг последней стадии)
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        # Создает список томатов
        self.tomatoes = [Tomato(i) for i in range(1, num_tomatoes + 1)]

    def grow_all(self):
        # Переводит все томаты на следующую стадию
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, все ли томаты созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает список томатов после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # name - публичное свойство (имя садовника)
        # _plant - защищенное свойство (объект класса TomatoBush)
        self.name = name
        self._plant = plant  # Изменено на _plant

    def work(self):
        # Садовник работает - растение растет
        print(f'Садовник {self.name} ухаживает за растениями...')
        self._plant.grow_all()

    def harvest(self):
        # Сбор урожая, если все томаты созрели
        if self._plant.all_are_ripe():
            print(f'Садовник {self.name} собирает урожай!')
            self._plant.give_away_all()
            return True
        else:
            print(f'Садовник {self.name}: Томаты еще не созрели!')
            return False

    @staticmethod
    def knowledge_base():
        # Справка по садоводству
        print('=' * 50)
        print('СПРАВКА ПО САДОВОДСТВУ:')
        print('1. Томаты проходят 4 стадии созревания:')
        for key, value in Tomato.states.items():
            print(f'   Стадия {key} - {value}')
        print('2. Садовник должен ухаживать за растениями')
        print('3. Урожай можно собрать, когда все томаты созреют')
        print('=' * 50)


if __name__ == "__main__":
    # Вызываем справку по садоводству
    Gardener.knowledge_base()

    # Создаем объекты классов TomatoBush и Gardener
    bush = TomatoBush(3)  # Куст с 3 томатами
    gardener = Gardener("Мария", bush)

    print("\nСадовник начинает работать")

    # Ухаживаем за кустом с помидорами
    gardener.work()

    # Пробуем собрать урожай (еще не дозрели)
    print("\nПробуем собрать урожай:")
    gardener.harvest()

    # Продолжаем ухаживать
    print("\nПродолжаем ухаживать за помидорами:")
    gardener.work()
    gardener.work()

    # Собираем урожай (после полного созревания)
    print("\nПоследняя попытка собрать урожай:")
    if gardener.harvest():
        print("Урожай собран!")
    else:
        print("Уроай собрать не получилось")
