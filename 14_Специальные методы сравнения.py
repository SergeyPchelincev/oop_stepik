
class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        print('__eq__ call')
        return self.price == other

    def __lt__(self, other):
        print('__lt__ call')
        if isinstance(other, (int, float)):
            return self.price < other
        elif isinstance(other, Fruit):
            return self.price < other.price

    def __ge__(self, other):
        print('__ge__ call')
        return self == other or self < other





# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
# assert (banana >= 1.2) is True
# assert (banana == 1.2) is False
# assert (banana != 1.2) is True
# assert (banana < 1.2) is False
# assert (banana <= 1.2) is False

# assert (apple > orange) is False
# assert (apple >= orange) is False
# assert (apple == orange) is False
# assert (apple != orange) is True
# assert (apple < orange) is True
# assert (apple <= orange) is True
#
# assert (orange == lime) is True
# assert (orange != lime) is False
# assert (orange > lime) is False
# assert (orange < lime) is False
# assert (orange <= lime) is True
# assert (orange >= lime) is True
# print('Good')
