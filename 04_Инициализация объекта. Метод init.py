# # Напишите определение класса SoccerPlayer
# class SoccerPlayer():
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
#
# # Ниже код для проверки методов класса SoccerPlayer
# leo = SoccerPlayer('Leo', 'Messi')
# assert isinstance(leo, SoccerPlayer)
# assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
# leo.score(700)
# assert leo.goals == 700
# leo.make_assist(500)
# assert leo.assists == 500
#
# leo.statistics()
#
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# assert isinstance(kokorin, SoccerPlayer)
# assert kokorin.name == 'Alex'
# assert kokorin.surname == 'Kokorin'
# assert kokorin.assists == 0
# assert kokorin.goals == 0
# kokorin.score()
# assert kokorin.goals == 1
# kokorin.score(5)
# assert kokorin.goals == 6
# kokorin.make_assist()
# assert kokorin.assists == 1
# kokorin.make_assist(10)
# assert kokorin.assists == 11
#
# kokorin.statistics()
#
#
# obi = SoccerPlayer('Оби-Ван', 'Кеноби')
# obi.make_assist()
# assert obi.name == 'Оби-Ван'
# assert obi.surname == 'Кеноби'
# assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
# obi.statistics()
#
# mila = SoccerPlayer('Mila', 'Kunis')
# mila.make_assist()
# mila.statistics()


# class Zebra():
#     list_examp = []
#
#     def which_stripe(self):
#         self.color1 = 'Полоска белая'
#         self.color2 = 'Полоска черная'
#
#         # Если список не пустой
#         if self.list_examp:
#             # 1. Если экземпляр уже есть в списке
#             if self in self.list_examp:
#                 print(self.color2)
#                 self.list_examp.remove(self)
#             # 2 Если экземпляра нет в списке
#             else:
#                 print(self.color1)
#                 self.list_examp.append(self)
#         # Если список пустой
#         else:
#             print(self.color1)
#             self.list_examp.append(self)
#
#
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"
#
# z3 = Zebra()
# z3.which_stripe() # печатает "Полоска белая"
# z3.which_stripe() # печатает "Полоска черная"


class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True