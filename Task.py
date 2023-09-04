#Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("ФИО должно начинаться с заглавной буквы и может содержать только буквы")
        setattr(instance, self._name, value)

class Student:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def print(self):
        print(self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

Student('Иванов', 'Иван', 'Иванович').print()
Student('иванов', 'И2ван', 'Иванович').print()