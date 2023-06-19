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


# # Напишите определение класса Employee
# class Employee:
#
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     def __get_name(self):
#         return self.__name
#
#     def __get_salary(self):
#         return self.__salary
#
#     def __set_salary(self, value):
#         if isinstance(value, (int, float)) and value > 0:
#             self.__salary = value
#         else:
#             print(f'ErrorValue:{value}')
#
#     title = property(fget=__get_name)
#     reward = property(fget=__get_salary, fset=__set_salary)

# import re
#
# class UserMail:
#
#     def __init__(self, login: str, email: str):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_email: str):
#         if isinstance(new_email, str) and len(re.findall(r'@.*\.', new_email)) == 1 and len(re.findall(r'@', new_email)) == 1:
#             self.__email = new_email
#         else:
#             print(f"ErrorMail:{new_email}")
#
#     email = property(fget=get_email, fset=set_email)
#
#
# # Ниже код для проверки методов класса UserMail
#
# jim = UserMail("aka47", 'hello@com.org')
# assert jim.login == "aka47"
# assert jim._UserMail__email == "hello@com.org"
# assert isinstance(jim, UserMail)
# assert isinstance(type(jim).email, property), 'Вы не создали property email'
#
# jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
# jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
# jim.email = 'hello@re.w3'
# assert jim.email == 'hello@re.w3'
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# assert k.email == 'prince@wait.you'
# assert k.login == 'belosnezhka'
# assert isinstance(k, UserMail)
#
# k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
# k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
# k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
# k.email = 'prince@still.wait'
# assert k.get_email() == 'prince@still.wait'
# k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
# assert k.email == 'prince@still.wait'



