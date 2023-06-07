
# class Notebook:
#
#     def __init__(self, list_val: list):
#         self._notes = list_val
#
#     @property
#     def notes_list(self):
#         for numb, val in enumerate(self._notes, 1):
#             print(f'{numb}.{val}')
#
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list


# class Money:
#
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, new_dollars):
#         if isinstance(new_dollars, int) and new_dollars >= 0:
#             self.total_cents = new_dollars * 100 + self.cents
#         else:
#             print("Error dollars")
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, new_cents):
#         if isinstance(new_cents, int) and 0 <= new_cents < 100:
#             self.total_cents = self.dollars * 100 + new_cents
#         else:
#             print("Error cents")
#
#     def __str__(self):
#         return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
#
#
# Bill = Money(101, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# print(Bill.total_cents) # 10199
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов




"""Вычисляемые свойства"""


# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @property
#     def area(self):
#         return self.length * self.width
#
# # Ниже код для проверки методов класса Rectangle
#
#
# r1 = Rectangle(5, 10)
# assert isinstance(r1, Rectangle)
# assert r1.area == 50
# assert isinstance(type(r1).area, property), 'Вы не создали property area'
#
# r2 = Rectangle(15, 3)
# assert isinstance(r2, Rectangle)
# assert r2.area == 45
# assert isinstance(type(r2).area, property), 'Вы не создали property area'
#
# r3 = Rectangle(43, 232)
# assert r3.area == 9976
# print('Good')


# class Date:
#
#     def __init__(self, d, m, y):
#         self.d = d
#         self.m = m
#         self.y = y
#
#     @property
#     def date(self):
#         return f'{self.d:02}/{self.m:02}/{self.y:04}'
#
#     @property
#     def usa_date(self):
#         return f'{self.m:02}-{self.d:02}-{self.y:04}'
#
# # Ниже код для проверки методов класса Date
#
# d1 = Date(5, 10, 2001)
# assert isinstance(d1, Date)
# assert d1.date == '05/10/2001'
# assert d1.usa_date == '10-05-2001'
# assert isinstance(type(d1).date, property), 'Вы не создали property date'
# print(d1.date, d1.usa_date)
#
# d2 = Date(15, 3, 999)
# assert isinstance(d2, Date)
# print(d2.date)
# assert d2.date == '15/03/0999'
# assert d2.usa_date == '03-15-0999'
# assert isinstance(type(d2).date, property), 'Вы не создали property date'
# print(d2.date, d2.usa_date)
#
# d3 = Date(3, 5, 3)
# assert d3.date == '03/05/0003'
# assert d3.usa_date == '05-03-0003'
# print(d3.date, d3.usa_date)

class Password:

    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        len_pass = len(str(self.password))
        if len_pass <= 8:
            return "Weak"
        elif 11 >= len_pass >= 8:
            return "Medium"
        return "Strong"

# Ниже код для проверки методов класса Password

pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"
assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"
pass_1.password = "123"
assert pass_1.strength == "Weak"
assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')
assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

