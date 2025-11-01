# Тема 8. Введение в ООП.
Отчет по Теме #8 выполнил(а):
* Макарова Мария Александровна 
* ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
* Ротенштрайх Т. В.

# Лабораторная работа
## Задание №1
Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car:  #создаем класс машин
    #создаем конструктор, которыйвызывается при создании новой машины и инициализирует переменные
    def __init__(self, make, model):
        self.make = make    #инициализируем переменную make (марка)
        self.model = model  #инициализируем переменную model (модель)

#Создаём новую машину
my_car = Car("Toyota", "Corolla")
```

# Результат
<img width="1161" height="569" alt="image" src="https://github.com/user-attachments/assets/bfe4b944-0916-4fd3-b576-afa268fe6223" />

# Вывод
Создали класс Car, в котором в конструкторе __init__ инициализировали переменные make и model. 

## Задание №2
Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```

# Результат
<img width="1169" height="746" alt="image" src="https://github.com/user-attachments/assets/be390ce0-983c-4d70-b857-d8d58f2cb948" />

# Вывод
Создали класс Car, в котором в конструкторе __init__ инициализировали переменные make и model. Затем создали метод drive, который выводит сообщение о том, что машина едет. 

## Задание №3
Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```

# Результат
<img width="1364" height="1080" alt="image" src="https://github.com/user-attachments/assets/2b813204-e0c7-4d31-949d-0a14b3771a39" />

# Вывод
Создали дочерний класс ElectricCar, который наследует от родительского класса Car конструктор и метод, при этом в самом новом классе также инициализируется свой конструктор, атрибут battery_capacity, который показываает ёемкость батареи, и метод charge, отвечающий за зарядку автомобиля. 

## Задание №4
Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```

# Результат 
<img width="1380" height="829" alt="image" src="https://github.com/user-attachments/assets/84f25b62-5778-46db-8c33-71a7a1fb778e" />

# Вывод
Создали класс Car, в котором в конструкторе __init__ инициализировали переменные _make как защищенный атрибут и __model как приватный атрибут. Затем создали метод drive, который выводит сообщение о том, что машина едет. При вызове print(my_car._make) выведется Toyota, а если попытаться вывести print(my_car.__model) мы получим ошибку. 

## Задание №5
Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```

# Результат
<img width="1379" height="1080" alt="image" src="https://github.com/user-attachments/assets/b58b488a-8df7-4452-b4a0-81e2ad087a13" />

# Вывод
Создаем родительский класс Shape с методом area, который переопределяется в классах-наследниках Rectangle и Circle. В Rectangle метод area возвращает произведение ширины и высоты, в Circle — вычисляет площадь по формуле π × r². При создании списка shapes с объектами обоих классов и проходе в цикле for shape in shapes вызов shape.area() автоматически выбирает соответствующую реализацию метода. 

# Самостоятельная работа
## Задание №1
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Flower:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

my_flower = Flower("Роза", "Красная")
print(f"Цветок {my_flower.name} имеет {my_flower.colour} цвет")
```

# Результат
<img width="813" height="571" alt="image" src="https://github.com/user-attachments/assets/13bca3cd-2bd4-47f3-905b-60d60563a850" />

# Вывод
Создаем класс Flower и конструктор с атрибутами name и colour, а затем выводим название нашего цветка и его цвет. 

## Задание №2
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```

# Результат
<img width="1202" height="710" alt="image" src="https://github.com/user-attachments/assets/5cb1aa69-9920-4d43-9674-394a64aa9b13" />

# Вывод
Создаем класс Flower и конструктор с атрибутами name, colour и height, а также метод grow, а затем выводим название нашего цветка, его цвет и рост, а также то, до какого роста он вырос. 

## Задание №3
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```

# Результат
<img width="1198" height="1002" alt="image" src="https://github.com/user-attachments/assets/fc95303a-89b1-4095-9c46-80f99c8443dc" />

# Вывод
Создаем класс Flower и конструктор с атрибутами name, colour и height, а также метод grow. Далее создаем дочерний класс Rose, у которого создаем свой конструктор и добовляем новый атрибут thorns и новый метод rose_have_thorns. Затем выводим название нашего цветка, его цвет и рост, а также то, есть ли у него шипы или нет. 

## Задание №4
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```

# Результат
<img width="1201" height="1080" alt="image" src="https://github.com/user-attachments/assets/7fd11edc-439b-42c5-8989-958fe4447808" />
<img width="1201" height="1080" alt="image" src="https://github.com/user-attachments/assets/2efbfbd2-3633-47f7-bef8-f124a534c4e1" />

# Вывод
Создали класс Flower с помощью конструктора init для установки свойств и декоратора @property для создания свойств name, colour, height. Метод grow() добавляет рост цветку с проверкой через raise ValueError. Создали класс Rose, который наследует от Flower через super().init, добавили свойства thorns и методы has_thorns(), describe_thorns(). Создали объект my_flower и вывели информацию о нем с помощью print(), а также вызвали метод grow() для увеличения роста.

## Задание №5
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```

# Результат
<img width="961" height="1080" alt="image" src="https://github.com/user-attachments/assets/44e9a086-8af6-4f60-92f7-9f40074313b6" />
<img width="961" height="1080" alt="image" src="https://github.com/user-attachments/assets/86d632a5-0780-46c6-8b34-482b45d386b8" />
<img width="962" height="1080" alt="image" src="https://github.com/user-attachments/assets/82a5ad45-0af8-4825-9e10-df9d1f116d14" />

# Вывод
Создали класс Flower с конструктором init и свойствами через декоратор @property. Добавили метод grow() с проверкой через raise ValueError и метод bloom(). Создали классы Rose, Sunflower и Tulip, которые наследуют от Flower через super().init и переопределяют метод bloom(). Функция make_flowers_bloom() с помощью цикла for вызывает метод bloom() для каждого цветка. Создали объекты цветков, поместили в список и вызвали функцию make_flowers_bloom(), затем вывели информацию о каждом цветке с помощью print() и увеличили их рост методом grow().

# Общий вывод
В ходе выполнения данный лабороторных и самостоятельных заданий мы научились работать с классами (создавать классы, конструкторы, атрибуты и методы), а также изучили ключевые принципы объектно-ориентированного программирования: абстракция, полиморфизм, инкапсуляцию и наследование. Ещё, мы попробовали поработать с геттерами и сеттерами. 
