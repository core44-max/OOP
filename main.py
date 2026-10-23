from service import FullTimeEmployee, PartTimeEmployee
from interface import Employee


def print_salary(employee: Employee):
    print(f'{employee.name}: {employee.calculate_salary()} somm')


fte = FullTimeEmployee("Arsen", 80000)
pte = PartTimeEmployee("Alina", 90, 800)
print_salary(fte)
print_salary(pte)
