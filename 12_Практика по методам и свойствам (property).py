import string


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_login):
        import re
        if not isinstance(new_login, str):
            raise TypeError
        if '@' not in new_login:
            raise ValueError
        if not re.findall(r'@.*\.', new_login):
            raise ValueError
        self.__login = new_login

    @staticmethod
    def is_include_digit(new_password):
        for digit in new_password:
            if digit in string.digits:
                return True
        return False

    @staticmethod
    def is_include_all_register(new_password):
        result_low = 0
        result_up = 0
        for symbol in new_password:
            if symbol in string.ascii_lowercase:
                result_low = 1
            if symbol in string.ascii_uppercase:
                result_up += 1
        if result_up and result_low:
            return True
        return False

    @staticmethod
    def is_include_only_latin(new_password):
        for symbol in new_password:
            if symbol not in string.digits and symbol not in string.ascii_letters:
                return False
            return True

    @staticmethod
    def check_password_dictionary(new_password):
        list_easy_password = []
        with open(r'easy_passwords.txt', 'r') as file:
            for string_file_txt in file:
                list_easy_password.append(string_file_txt.strip())
        if new_password in list_easy_password:
            return True
        return False

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError  # ("Пароль должен быть строкой")
        if not 4 < len(new_password) < 12:
            raise ValueError  # ('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(new_password):
            raise ValueError  # ('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(new_password):
            raise ValueError  # ('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(new_password):
            raise ValueError  # ('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(new_password):
            raise ValueError  # ('Ваш пароль содержится в списке самых легких')
        self.__password = new_password


# a = Registration('name_mercy@mail.ru', 'QwerTy123')
# print(a.password)

print(Registration.check_password_dictionary('QwerTy123'))
