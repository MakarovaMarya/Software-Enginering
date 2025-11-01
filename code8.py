class Car:  #создаем класс машин
    #создаем конструктор, которыйвызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model):
        self.make = make    #инициализируем переменную make (марка)
        self.model = model  #инициализируем переменную model (модель)

#Создаём новую машину
my_car = Car("Toyota", "Corolla")


class Car:  #создаем класс машин
    #создаем конструктор, который вызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model):
        self.make = make    #инициализируем переменную make (марка)
        self.model = model  #инициализируем переменную model (модель)

    def drive(self):  #создаем метод, отвечающий за движение автомобиля
        print(f"Driving the {self.make} {self.model}")  #выводим сообщение о движении

#создаём новую машину
my_car = Car("Toyota", "Corolla")
#вызываем метод drive
my_car.drive()


class Car:  #создаем класс машин
    #создаем конструктор, который вызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model):
        self.make = make    #инициализируем переменную make (марка)
        self.model = model  #инициализируем переменную model (модель)

    def drive(self):  #создаем метод, отвечающий за движение автомобиля
        print(f"Driving the {self.make} {self.model}")  #выводим сообщение о движении

#создаём новую машину
my_car = Car("Toyota", "Corolla")
#вызываем метод drive
my_car.drive()

class ElectricCar(Car):  # Создаем класс электроавтомобилей, который наследуется от класса Car
    #создаем конструктор, который вызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  #вызываем конструктор родительского класса
        self.battery_capacity = battery_capacity  #добавляем емкость батареи

    def charge(self):  #создаем метод, отвечающий за зарядку электромобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") #выводим сообщение о зарядке

#создаем объект электромобиль
my_electric_car = ElectricCar("Tesla", "Model S", 75)
#вызываем метод из родительского класса - машина едет
my_electric_car.drive()
#вызываем собственый метод charge - машина заряжается
my_electric_car.charge()


class Car:  #создаем класс машин
    #создаем конструктор, которыйвызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model):
        self._make = make    #инициализируем переменную make (марка)
        self.__model = model  #инициализируем переменную model (модель)

    def drive(self):  # создаем метод, отвечающий за движение автомобиля
        print(f"Driving the {self._make} {self.__model}")  # выводим сообщение о движении

#Создаём новую машину
my_car = Car("Toyota", "Corolla")
print(my_car._make) # Доступ к защищенному атрибуту
# print(my_car.__model)  # Ошибка! Приватный атрибут не доступен напрямую
#вызываем метод drive
my_car.drive()


class Shape:  #создаем основной (общий) класс
    def area(self):  #создаем метод для подсчета площади
        pass  #используем заглушку, т.к. метод больше ничего не делает

class Rectangle(Shape):  #создаем класс Прямоугольник, который наследуется от Shape
    def __init__(self, width, height):  #создаем конструктор
        self.width = width    #ширина
        self.height = height  #высота
    def area(self):  #переопределяем метод area из родительского класса для прямоугольника
        return self.width * self.height  #площадь = ширина * высоту

class Circle(Shape):  #создаем класс Круг, который наследуется от Shape
    def __init__(self, radius):  #создаем конструктор
        self.radius = radius  #радиус круга
    def area(self):  #переопределяем метод из родительского класса area для круга
        return 3.14 * self.radius * self.radius  #площадь = π × r²

#создаем массив
shapes = [Rectangle(9, 9), Circle(9)]  #прямоугольник 9 на 9 и круг радиусом 9

#выводим площади фигур в цикле
for shape in shapes:
    print(f"Area: {shape.area()}")  #полиморфизм: вызывается нужный метод area()




class Flower:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

my_flower = Flower("Роза", "Красная")
print(f"Цветок {my_flower.name} имеет {my_flower.colour} цвет")


class Flower:
    def __init__(self, name, colour, height):
        self.name = name
        self.colour = colour
        self.height = height
    def grow(self, height):
        print(f"Цветок {my_flower.name} вырос до {height}!")

my_flower = Flower("Роза", "Красная", 20)
print(f"Цветок {my_flower.name} имеет {my_flower.colour} цвет и рост {my_flower.height} сантиметров")
my_flower.grow(30)


class Flower:
    def __init__(self, name, colour, height):
        self.name = name
        self.colour = colour
        self.height = height
    def grow(self, height):
        print(f"Цветок {my_flower.name} вырос до {height}!")

class Rose(Flower):
    def __init__(self, name, colour, height, thorns):
        super().__init__(name, colour, height)
        self.thorns = thorns
    def rose_have_thorns(self, thorns):
        if (thorns == True):
            print(f"У этой розы есть шипы")
        else:
            print(f"У этой розы нет шипов")

my_flower = Rose("Роза", "красный", 20, True)
print(f"Цветок {my_flower.name} имеет {my_flower.colour} цвет и рост {my_flower.height} сантиметров")
my_flower.rose_have_thorns(True)


class Flower:
    def __init__(self, name, colour, height):
        self._name = name
        self._colour = colour
        self._height = height
    @property
    def name(self):
        return self._name
    @property
    def colour(self):
        return self._colour
    @property
    def height(self):
        return self._height
    def grow(self, growth):
        if growth <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self._height += growth
        print(f"Цветок {self._name} вырос до {self._height} см!")

class Rose(Flower):
    def __init__(self, name, colour, height, thorns):
        super().__init__(name, colour, height)
        self._thorns = thorns
    @property
    def thorns(self):
        return self._thorns
    def has_thorns(self):
        return self._thorns
    def describe_thorns(self):
        if self._thorns:
            return "У этой розы есть шипы"
        else:
            return "У этой розы нет шипов"

my_flower = Rose("Роза", "красный", 20, True)
print(f"Цветок {my_flower.name} имеет {my_flower.colour} цвет и рост {my_flower.height} сантиметров")
print(my_flower.describe_thorns())
my_flower.grow(9)


class Flower:
    def __init__(self, name, colour, height):
        self._name = name
        self._colour = colour
        self._height = height
    @property
    def name(self):
        return self._name
    @property
    def colour(self):
        return self._colour
    @property
    def height(self):
        return self._height
    def grow(self, growth):
        if growth <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self._height += growth
        print(f"Цветок {self._name} вырос до {self._height} см!")
    def bloom(self):
        return f"{self._name} цветет"

class Rose(Flower):
    def __init__(self, name, colour, height, thorns):
        super().__init__(name, colour, height)
        self._thorns = thorns
    @property
    def thorns(self):
        return self._thorns
    def has_thorns(self):
        return self._thorns
    def describe_thorns(self):
        if self._thorns:
            return "У этой розы есть шипы"
        else:
            return "У этой розы нет шипов"
    def bloom(self):
        return f"{self._name} распускается красивыми {self._colour} бутонами"

class Sunflower(Flower):
    def __init__(self, name, colour, height):
        super().__init__(name, colour, height)
    def bloom(self):
        return f"{self._name} поворачивается к солнцу"


class Tulip(Flower):
    def __init__(self, name, colour, height):
        super().__init__(name, colour, height)
    def bloom(self):
        return f"{self._name} нежно колышется на ветру"

def make_flowers_bloom(flowers):
    for flower in flowers:
        print(flower.bloom())

rose = Rose("Роза кустовая", "красный", 20, True)
sunflower = Sunflower("Подсолнух", "желтый", 150)
tulip = Tulip("Тюльпан", "розовый", 30)

flowers = [rose, sunflower, tulip]
make_flowers_bloom(flowers)

for flower in flowers:
    print(f"{flower.name}, цвет: {flower.colour}, высота: {flower.height}см")

for flower in flowers:
    flower.grow(10)
