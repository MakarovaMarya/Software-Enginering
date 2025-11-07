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


