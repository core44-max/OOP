# Класс это структура данных, которая служит для описания объектов
class Person:
    name: str = "Asan"  # свойство -> атрибут
    age: int = 25  # свойство -> атрибут

    def sleep(self):
        print(f"{self.name} спит")

    def run(self):
        print(f"{self.name} runing")


person_1 = Person()  # first object
print(person_1.name)
print(person_1.age)
person_1.sleep()

person_2 = Person()
person_2.name = "Uson"
person_2.age = 22
print(person_2.name)
print(person_2.age)
person_2.run()
print(person_1.name)
print(person_2.name)
