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
