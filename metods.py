from builtins import staticmethod, classmethod


class Car:
    count = 0
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def info(self):
        print(f'Model: {self.model}')
        print(f'year: {self.year}')
    @staticmethod
    def get_class_details():
        print("Это класс Car")
    @classmethod
    def get_class_attr(cls):
        cls.count = 1
Car.get_class_details()
car_1 = Car(model="Toyota", year=2020)
car = Car(model="BMW", year=2021)
car.info()
car_1.info()

