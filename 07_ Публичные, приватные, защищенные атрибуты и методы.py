
# class AverageCalculator:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def __calculate_average(self):
#         total = sum(self.numbers)
#         return total / len(self.numbers)
#
#
# average_calculator = AverageCalculator([1, 2, 3])
# print(dir(average_calculator))
# print(average_calculator._AverageCalculator__calculate_average())


# class Student:
#
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()


# class BankDeposit:
#
#     def __initi__(self, name, balance, rate):
#         self.name = name
#         self.balance = balance
#         self.rate = rate
#
#     def __calculate_profit(self):
#         return self.balance * (self.rate / 100)
#
#     def get_balance_with_profit(self):
#         return self.balance + self.__calculate_profit()

# class Library:
#
#     def __init__(self, books):
#         self.__books = books
#
#     def __check_availability(self, name_book):
#         if name_book in self.__books:
#             return True
#         return False
#
#     def search_book(self, name_book):
#         if self.__check_availability(name_book):
#             return True
#         return False
#
#     def return_book(self, append_book):
#         self.__books.append(append_book)
#
#     def _checkout_book(self, name_book):
#         if name_book in self.__books:
#             self.__books.remove(name_book)
#             return True
#         return False
#
# # Ниже код для проверки методов класса Library
# library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
#
# assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
# assert library.search_book("Moby-Dick") == True
# assert library.search_book("Jane Air") == False
#
# assert library._Library__check_availability("War and Peace") == True
# assert library._checkout_book("Moby-Dick") == True
# assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
#
# assert library.search_book("Moby-Dick") == False
# assert library.return_book("Moby-Dick") is None
# assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
# assert library.search_book("Moby-Dick") == True
# print('Good')

class Employee:

    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self, up_pos):
        self.__position = up_pos

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"

# Ниже код для проверки методов класса Employee
employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'

employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
assert employee_2._Employee__calculate_salary() == 1050
assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

print('Good')