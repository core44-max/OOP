# Инкапсуляция 3 доступу
# public
# private -> __
# protect -> -
from os import name


class Person:
    def __init__(self):
        self.name = "Asan"  # public
        self.__passwaord = "12345"  # private
        self._year = 2000  # protect
        self.__Name = "Erbol"

    def get_password(self):
        return self.__passwaord

    def set_password(self, password):
        self.__passwaord = password


obj = Person()
print(obj.name)
print(obj._year)
print(obj.get_password())
obj.set_password("123")
print(obj.get_password())

