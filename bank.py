class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Пополнено: {amount}')
        else:
            print('Сумма должна быть положительной')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Снято: {amount}')
        else:
            print(f'Нетостаточно средсвт или некорректная сумма')

    def get_balance(self):
        return self.__balance

arsen = BankAccount("Arsen", 1000)
print(arsen.get_balance())
arsen.deposit(500)
arsen.withdraw(800)
print(arsen.get_balance())

arsen.withdraw(1000)
print(arsen.get_balance())
