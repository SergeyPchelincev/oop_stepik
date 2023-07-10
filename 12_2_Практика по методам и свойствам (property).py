class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, plus_balance):
        self.__balance += plus_balance

    def payment(self, minus_balance):
        if self.__balance < minus_balance:
            print(f'Не хватает средств на балансе. Пополните счет')
            return False
        self.__balance -= minus_balance
        return True


class Cart:
    list_price_product = []

    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, number_of_goods=1):
        if product in self.goods:
            self.goods[product] += number_of_goods
        else:
            self.goods[product] = number_of_goods
            # Добавляю в список класса цену объекта и его название
            Cart.list_price_product.append([product.price, product])
        self.__total += product.price * number_of_goods

    def remove(self, product, number_of_goods=1):
        if self.goods[product] >= number_of_goods:
            self.goods[product] -= number_of_goods
        else:
            for numb, object_param in enumerate(Cart.list_price_product):
                if product in object_param:
                    price_prod = object_param[0]
                    del Cart.list_price_product[numb]
            total_prod = self.goods[product] * price_prod
            self.goods.pop(product)

        if total_prod:
            self.__total -= total_prod
        else:
            self.__total >= product.price
            self.__total -= product.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for key_goods, value_goods in sorted(self.goods.items(), key=lambda x: x[0].name):
            for list_prod in Cart.list_price_product:
                if key_goods in list_prod:
                    print(f'{key_goods.name} {list_prod[0]} {value_goods} {list_prod[0]*value_goods}')
                    # {Имя товара} {Цена товара} {Количество товара} {Сумма}
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
