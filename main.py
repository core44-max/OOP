# Наследования
# Полиморфизм
# Инкапсуляция
from builtins import setattr


# PEP8 -> это руководство на написанию кода на языке Python

class Point:
    """Класс для представления координат точек на плоскости"""
    x: int = 1
    y: int = 2

# getattr(obj, name, [default]) # get attribute
# hasattr(obj, name)
# setattr(obj, name, value)
# delattr(obj, name)

p1 = Point()
p2 = Point()
print(getattr(p1, 'x'))
print(getattr(p1, 'y'))
try:
    print(getattr(p1, 'z'))
except AttributeError:
    setattr(p1, 'z', 3)
print(getattr(p1, 'z'))

if not hasattr(p2, 'z'):
    setattr(p2, 'z', 6)
print(getattr(p2, 'z'))
print(getattr(p2, 'i', 'attribute i not found'))
delattr(p2, 'z')
print(getattr(p2, 'z'))
