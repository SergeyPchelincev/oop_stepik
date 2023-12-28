
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')
#
# class Bus(Vehicle):
#     pass
#
# # Ниже располагается код для проверки
#
# assert issubclass(Bus, Vehicle)
# bus_99 = Bus("Ikarus", 66, 124567)
# assert bus_99.name == 'Ikarus'
# assert bus_99.max_speed == 66
# assert bus_99.mileage == 124567
# bus_99.display_info()
#
# modelX = Vehicle('modelX', 240, 18)
# assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
# modelX.display_info()
#
# audi = Bus('audi', 123, 43)
# assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
# audi.display_info()


# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def is_employee(self):
#         return False
#
# class Employee(Person):
#
#     def is_employee(self):
#         return True
#
# # Ниже располагается код для проверки
# assert issubclass(Employee, Person)
#
# p = Person("just human")
# assert p.name == 'just human'
# assert p.get_name() == 'just human'
# assert p.is_employee() is False
#
# emp = Employee("Geek")
# assert emp.name == 'Geek'
# assert emp.get_name() == 'Geek'
# assert emp.is_employee() is True
# print('Good')


# напишите определение классов
class Shape:
    pass

class Polygon(Shape):
    pass
class Triangle(Polygon):
    pass

class Ellipse(Shape):
    pass
class Circle(Ellipse):
    pass

class Rectangle(Polygon):
    pass
class Square(Rectangle):
    pass

shapes = [
    Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
    Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
    Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
    Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
    Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
    Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
    Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
    Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
    Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
    Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
    Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
    Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
    Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
    Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
]


quantity_circle = 0
quantity_rectangle = 0
quantity_polygon = 0
for el in shapes:
    if isinstance(el, Circle):
        quantity_circle += 1
    elif isinstance(el, Rectangle):
        quantity_rectangle += 1
    elif isinstance(el, Polygon):
        quantity_polygon += 1

quantity_polygon += quantity_rectangle
print(quantity_circle)
print(quantity_rectangle)
print(quantity_polygon)