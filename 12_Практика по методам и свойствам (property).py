# import string
#
#
# class Registration:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @property
#     def password(self):
#         return self.__password
#
#     @login.setter
#     def login(self, new_login):
#         import re
#         if not isinstance(new_login, str):
#             raise TypeError
#         if '@' not in new_login:
#             raise ValueError
#         if not re.findall(r'@.*\.', new_login):
#             raise ValueError
#         self.__login = new_login
#
#     @staticmethod
#     def is_include_digit(new_password):
#         for digit in new_password:
#             if digit in string.digits:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(new_password):
#         result_low = 0
#         result_up = 0
#         for symbol in new_password:
#             if symbol in string.ascii_lowercase:
#                 result_low = 1
#             if symbol in string.ascii_uppercase:
#                 result_up += 1
#         if result_up and result_low:
#             return True
#         return False
#
#     @staticmethod
#     def is_include_only_latin(new_password):
#         for symbol in new_password:
#             if symbol not in string.digits and symbol not in string.ascii_letters:
#                 return False
#             return True
#
#     @staticmethod
#     def check_password_dictionary(new_password):
#         list_easy_password = []
#         with open(r'easy_passwords.txt', 'r') as file:
#             for string_file_txt in file:
#                 list_easy_password.append(string_file_txt.strip())
#         if new_password in list_easy_password:
#             return True
#         return False
#
#     @password.setter
#     def password(self, new_password):
#         if not isinstance(new_password, str):
#             raise TypeError  # ("Пароль должен быть строкой")
#         if not 4 < len(new_password) < 12:
#             raise ValueError  # ('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if not Registration.is_include_digit(new_password):
#             raise ValueError  # ('Пароль должен содержать хотя бы одну цифру')
#         if not Registration.is_include_all_register(new_password):
#             raise ValueError  # ('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         if not Registration.is_include_only_latin(new_password):
#             raise ValueError  # ('Пароль должен содержать только латинский алфавит')
#         if Registration.check_password_dictionary(new_password):
#             raise ValueError  # ('Ваш пароль содержится в списке самых легких')
#         self.__password = new_password
#
#
# # a = Registration('name_mercy@mail.ru', 'QwerTy123')
# # print(a.password)
#
# print(Registration.check_password_dictionary('QwerTy123'))


class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        self.in_trash = False
        print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        self.is_deleted = True
        print(f'Файл {self.name} был удален')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        if not self.is_deleted and not self.in_trash:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        if not self.is_deleted and not self.in_trash:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print('В корзину добавлять можно только файл')
        else:
            Trash.content.append(file)
            file.in_trash = True

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for k in Trash.content:
            File.remove(k)
        Trash.content.clear()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for k in Trash.content:
            File.restore_from_trash(k)
        Trash.content.clear()
        print('Корзина пуста')

# С предыдущего урока у вас должен быть создан класс  File, у которого имеется:
#
# метод __init__
# метод  restore_from_trash
# метод  remove
# метод read
# метод write
# Далее создайте класс  Trash у которого есть:
#
# атрибут класса  content изначально равный пустому списку
#
# статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут content
# и проставить файлу атрибут in_trash значение True. Если в метод add передается не экземпляр класса File,
# необходимо вывести сообщение «В корзину добавлять можно только файл»
#
# статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов,
# хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove. Атрибут content  после
# очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой «Очищаем корзину» и
# заканчиваться фразой «Корзина пуста»
#
# статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов,
# хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash.
# Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться
#  фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»

# Ниже код для проверки класса File и Trash

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content


Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()
# 11111111
print('00000000000000000000000000000000')