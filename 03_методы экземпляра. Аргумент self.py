# # 1.Напишите определение класса Robot
# class Robot():
#
#     def set_name(self, name):
#         self.name = name
#
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print('У робота нет имени')
#
#     def say_bye(self):
#         print('See u later alligator')
#
#
# # Ниже код для проверки класса Robot
#
# c3po = Robot()
# c3po.say_hello()
# c3po.set_name('R2D2')
# c3po.say_hello()
# c3po.say_bye()


# # 2.Напишите определение класса Constructor
# class Constructor():
#
#     def add_atribute(self, name, value):
#         setattr(self, name, value)
#
#     def display(self):
#         print(self.__dict__)
#
#
# # Ниже код для проверки класса Constructor
#
# obj1 = Constructor()
# assert obj1.__dict__ == {}
# obj1.display()
# obj1.add_atribute('color', 'red')
# print(obj1.__dict__)
# assert obj1.color == 'red'
# obj1.add_atribute('width', 20)
# assert obj1.width == 20
# obj1.display()


# 3.
class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self1, self2):
        if isinstance(self2, Point):
            diff_x = self2.x - self1.x
            diff_y = self2.y - self1.y
            d = (diff_x ** 2 + diff_y ** 2) ** .5
            return d
        else:
            print("Передана не точка")



# Код ниже не удаляйте, он нужен для проверок
p1 = Point()
p2 = Point()
assert isinstance(p1, Point)
assert isinstance(p2, Point)

p1.set_coordinates(1, 2)
assert p1.x == 1
assert p1.y == 2
p2.set_coordinates(4, 6)
assert p2.x == 4
assert p2.y == 6
assert p1.get_distance(p2) == 5.0
p3 = Point()
p3.set_coordinates(10, 10)
p1.set_coordinates(4, 2)
assert p1.get_distance(p3) == 10.0
res = p1.get_distance(10)  # Распечатает "Передана не точка", вернет None
assert res is None, 'Метод get_distance должен возвращать None, если в него была передана не точка'

assert p2.get_distance([1, 2, 3]) is None  # Распечатает "Передана не точка", вернет None