#
# # Напишите определение класса TemperatureConverter
# class TemperatureConverter:
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         fahrenheit = celsius * 9/5 + 32
#         return fahrenheit
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         celsius = (fahrenheit-32) * 5 / 9
#         return celsius
#
# # Ниже код для проверки методов класса TemperatureConverter
# assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
# assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
# assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
# assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
# assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
# assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0
#
# assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
# assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
# assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
# assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
# assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
# assert TemperatureConverter.fahrenheit_to_celsius(32) == 0
# print('Good')


# class RobotVacuumCleaner:
#     name = 'Henry'
#     charge = 25
#
#     @classmethod
#     def update_charge(cls, new_value):
#         cls.charge = new_value
#
#     @staticmethod
#     def hello(name):
#         return f'Привет, {name}'
#
#     @property
#     def data(self):
#         return {
#             'name': self.name,
#             'charge': self.charge
#         }
#
#     def make_clean(self):
#         if self.charge < 30:
#             return 'Кожаный, заряди меня! Я слаб'
#         return 'Я вычищу твою берлогу!!!'
#
# # код ниже не нужно удалять, в нем находятся проверки
# print(RobotVacuumCleaner.hello('Господин'))
# RobotVacuumCleaner.update_charge(50)
#
# robot = RobotVacuumCleaner()
# print(robot.make_clean())
# print(robot.data)
#
# RobotVacuumCleaner.update_charge(False)
# print(robot.make_clean())



