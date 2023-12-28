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
#
#
# class UnitedKingdom:
#
#     def get_capital(self):
#         print("London is the capital of Great Britain.")
#
#     def get_language(self):
#         print("English is the primary language of Great Britain.")
#
#
# class Spain:
#
#     def get_capital(self):
#         print("Madrid is the capital of Spain.")
#
#     def get_language(self):
#         print("Spanish is the primary language of Spain.")
#
# obj_uk = UnitedKingdom()
# obj_spa = Spain()
# for country in (obj_spa, obj_uk):
#     country.get_capital()
#     country.get_language()



# class Building:
#
#     def __init__(self, floor):
#         self.floor = {}
#         for k in range(floor):
#             self.floor[k+1] = None
#
#     def __setitem__(self, key, value):
#         self.floor[key] = value
#
#     def __getitem__(self, item):
#         return self.floor[item]
#
#     def __delitem__(self, key):
#         self.floor[key] = None
#
# iron_building = Building(22)  # Создаем здание с 22 этажами
# iron_building[0] = 'Reception'
# iron_building[1] = 'Oscorp Industries'
# iron_building[2] = 'Stark Industries'
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])

# class Song:
#
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#
# class Playlist:
#
#     def __init__(self):
#         self.songs = []
#
#     def __getitem__(self, item):
#         return self.songs[item]
#
#     def __setitem__(self, key, value):
#         self.songs.insert(key, value)
#
#     def add_song(self, object):
#         self.songs.append(object)

# # Ниже код для проверки методов классов Song и Playlist
#
# playlist = Playlist()
# assert len(playlist.songs) == 0
# assert isinstance(playlist, Playlist)
# playlist.add_song(Song("Paradise", "Coldplay"))
# assert playlist[0].title == 'Paradise'
# assert playlist[0].artist == 'Coldplay'
# assert len(playlist.songs) == 1
#
# playlist[0] = Song("Resistance", "Muse")
# assert playlist[0].title == 'Resistance'
# assert playlist[0].artist == 'Muse'
# assert playlist[1].title == 'Paradise'
# assert playlist[1].artist == 'Coldplay'
#
# playlist[1] = Song("Helena", "My Chemical Romance")
# assert playlist[1].title == 'Helena'
# assert playlist[1].artist == 'My Chemical Romance'
#
# assert playlist[2].title == 'Paradise'
# assert playlist[2].artist == 'Coldplay'
# print('Good')

class ShoppingCart:

    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        if item in self.items.keys():
            return self.items[item]
        return 0

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        self.items.pop(key)

    def add_item(self, name_item, quantity=1):
        if name_item in self.items.keys():
            self.items[name_item] += quantity
        else:
            self.items[name_item] = quantity

    def remove_item(self, name_product, qua_name=1):
        if name_product in self.items.keys():
            if self.items[name_product] <= qua_name:
                self.items.pop(name_product)
            else:
                self.items[name_product] -= qua_name


# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")
