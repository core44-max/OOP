class Parent:
    def earn_money(self):
        print("Родители зарабатывает")


class Mother:
    def earn_money(self):
        print("Мама зарабатывает")


class Father:
    def earn_money(self):
        print("Отец зарабатывает")


class Child(Father, Mother, Parent):
    # def earn_money(self):
    #     print("Ребенок зарабатывает")

    def play(self):
        print("Ребенок играет")

print(Child.mro())
obj = Child()
obj.play()
obj.earn_money()
