class Person:
    addres = "kyrgyzstan" # атрибут класса
    count = 0 # атрибут класса
    
    def setup(self, name, surname):
        self.name = name # атрибут экземпляра
        self.surname = surname # атрибут экземпляра
        Person.count += 1

    def info(self):
        print(self.name)
        print(self.surname)
        print(self.addres)
        print(self.count)
obj_1 = Person()
obj_2 = Person()
obj_1.setup(name="Asan", surname="Emilov")
obj_2.setup("Uson", "Emilov")
obj_1.info()
print("#" * 10)
obj_2.info()

