# # Напишите определение класса City
# class City:
#
#     def __init__(self, name):
#         self.name = City.name_latter(name)
#
#     @staticmethod
#     def name_latter(name):
#         name_new = ''
#         first_letter = 1
#         for letter in name:
#             if first_letter:
#                 name_new += letter.upper()
#                 first_letter = 0
#             elif letter == ' ':
#                 name_new += letter
#                 first_letter = 1
#             else:
#                 name_new += letter.lower()
#         return name_new
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         if self.name[-1] in ('a', 'e', 'i', 'o', 'u'):
#             return False
#         return True
#
# # Ниже код для проверки методов класса City
#
# p1 = City('new york')
# assert p1.name == "New York"
# assert p1.__str__() == "New York"
# assert isinstance(p1, City)
# print(p1)
# assert bool(p1)
#
# p2 = City('SaN frANCISco')
# assert isinstance(p2, City)
# assert p2.name == "San Francisco"
# print(p2)
# assert not bool(p2)
#
# p3 = City('NIZHNY NoVGORod')
# assert p3.name == "Nizhny Novgorod"
# print(p3)
# assert bool(p3)
# assert isinstance(p3, City)

# Напишите определение класса Quadrilateral
class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = self.height = width
        if height:
            self.height = height

    def __str__(self):
        if self.width != self.height:
            return f'Прямоугольник размером {self.width}х{self.height}'
        return f'Квадрат размером {self.width}х{self.height}'

    def __bool__(self):
        if self.width != self.height:
            return False
        return True

# Ниже код для проверки методов класса Quadrilateral

q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)