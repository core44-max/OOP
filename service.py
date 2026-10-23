from interface import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.__mothly_salary = monthly_salary

    def calculate_salary(self):
        return self.__mothly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate
