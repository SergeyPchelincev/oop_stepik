#
# class BankAccount:
#
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self):
#         return self._account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def set_balance(self, value):
#         self._balance = value


# Напишите определение класса Employee
class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__salary = value
        else:
            print(f'ErrorValue:{value}')

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)


