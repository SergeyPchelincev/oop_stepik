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


# # Напишите определение класса Quadrilateral
# class Quadrilateral:
#
#     def __init__(self, width, height=None):
#         self.width = self.height = width
#         if height:
#             self.height = height
#
#     def __str__(self):
#         if self.width != self.height:
#             return f'Прямоугольник размером {self.width}х{self.height}'
#         return f'Квадрат размером {self.width}х{self.height}'
#
#     def __bool__(self):
#         if self.width != self.height:
#             return False
#         return True
#
# # Ниже код для проверки методов класса Quadrilateral
#
# q1 = Quadrilateral(10)
# print(q1)
# assert q1.height == 10
# assert q1.width == 10
# assert bool(q1) is True
# assert q1.__str__() == "Квадрат размером 10х10"
# assert isinstance(q1, Quadrilateral)
#
# q2 = Quadrilateral(3, 5)
# print(q2)
# assert q2.__str__() == "Прямоугольник размером 3х5"
# assert bool(q2) is not True
# assert isinstance(q2, Quadrilateral)
#
# q3 = Quadrilateral(4, 7)
# print(q3)
# assert bool(q3) is False
# assert q3.__str__() == "Прямоугольник размером 4х7"
# assert isinstance(q3, Quadrilateral)


# # Напишите определение класса QuadraticFunction
# class QuadraticFunction:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, *args, **kwargs):
#         return self.a*args[0]**2 + self.b*args[0] + self.c
#
# # Ниже код для проверки методов класса QuadraticFunction
# f = QuadraticFunction(2, 5, 7)
# assert f(1) == 14
# assert f(-3) == 10
# assert f(2) == 25
# assert f(5) == 82
#
# f_2 = QuadraticFunction(-1, 2, 4)
# assert f_2(5) == -11
# assert f_2(2) == 4
# assert f_2(-3) == -11
# assert f_2(1) == 5
# print('Good')


# # Напишите определение класса Addition
# class Addition:
#
#     def __call__(self, *args, **kwargs):
#         sum = 0
#         for j in args:
#             if isinstance(j, (int, float)):
#                 sum += j
#         return f'Сумма переданных значений = {sum}'
#
# # Ниже код для проверки методов класса Addition
# add = Addition()
# assert add(10, 20) == "Сумма переданных значений = 30"
# assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
# assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"
#
#
# add2 = Addition()
# assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
# assert add2() == "Сумма переданных значений = 0"
# assert add2('hello') == "Сумма переданных значений = 0"
#
# print('Good')


class UnitedKingdom:

    def get_capital(self):
        print("London is the capital of Great Britain.")

    def get_language(self):
        print("English is the primary language of Great Britain.")


class Spain:

    def get_capital(self):
        print("Madrid is the capital of Spain.")

    def get_language(self):
        print("Spanish is the primary language of Spain.")

obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.get_capital()
    country.get_language()