#
# class Dog():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self,sound):
#         return f'{self.name} says {sound}'
#
# # Ниже код для проверки класса Dog
# curt = Dog("Curt", 4)
# assert isinstance(curt, Dog)
# assert curt.name == 'Curt'
# assert curt.age == 4
# assert curt.description() == 'Curt is 4 years old'
# assert curt.speak("Wo") == 'Curt says Wo'
# assert curt.speak("Bow") == 'Curt says Bow'
#
# jack = Dog("Jack", 12)
# assert isinstance(curt, Dog)
# assert jack.name == 'Jack'
# assert jack.age == 12
# assert jack.description() == 'Jack is 12 years old'
# assert jack.speak("Woof Woof") == 'Jack says Woof Woof'
# assert jack.speak("Bow Wow") == 'Jack says Bow Wow'
#
# assert Dog('Karl', 6).description() == 'Karl is 6 years old'
# print('Good')

# class Rectangle():
#
#     def __init__(self, width=0, height=0):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         s_area = self.width * self.height
#         return s_area
#
#     def perimeter(self):
#         p_area = (self.width + self.height) * 2
#         return p_area
#
# # Ниже код для проверки методов класса Rectangle
# r1 = Rectangle(2, 3)
# assert r1.width == 2
# assert r1.height == 3
# assert r1.perimeter() == 10
# assert r1.area() == 6
#
# r2 = Rectangle(10, 0.5)
# assert r2.width == 10
# assert r2.height == 0.5
# assert r2.perimeter() == 21.0
# assert r2.area() == 5.0
# print('Good')



# class Stack():
#
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if not self.values:
#             print('Empty Stack')
#             return None
#
#         else:
#             el = self.values[-1]
#             del self.values[-1]
#             return el
#
#     def peek(self):
#         if not self.values:
#             print('Empty Stack')
#             return None
#         else:
#             return self.values[-1]
#
#     def is_empty(self):
#         if not self.values:
#             return True
#         else:
#             return False
#
#     def size(self):
#         return len(self.values)
#
#
# # Ниже код для проверки класса Stack
#
# s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)
#
# s.peek()  # распечатает 'Empty Stack'
# assert s.is_empty() is True
# s.push('cat')
# assert s.size() == 1
# assert s.peek() == 'cat'
#
# s.push('dog')
# assert s.size() == 2
# assert s.peek() == 'dog'
#
# s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False
#
# s.push(777)
# assert s.size() == 4
#
# assert s.pop() == 777
# assert s.size() == 3
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
#
# d = Stack()
# assert d.peek() is None  # Печатает "Empty Stack"
# assert d.pop() is None  # Печатает "Empty Stack"
# d.push('hello')
# assert d.size() == 1
# d.push('world')
# assert d.size() == 2
# assert d.peek() == 'world'
# assert d.pop() == 'world'
# assert d.peek() == 'hello'



# class Worker():
#
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
#
# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# worker_objects = []
#
# for per in persons:
#     worker_objects.append(Worker(*per))
#
# for exemp in worker_objects:
#     exemp.get_info()


# class CustomLabel():
#
#     def __init__(self, text, **kwargs):
#         self.text = text
#         self.config(**kwargs)
#
#     def config(self, **kwargs_two):
#         for key_kw_two in kwargs_two:
#             setattr(self, key_kw_two, kwargs_two[key_kw_two])
#
# # Ниже код для проверки методов класса CustomLabel
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}


# class Person():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company():
#
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
# class Employee():
#
#     def __init__(self, name, age, company_name, location):
#         self.name = name
#         self.age = age
#         self.company_name = company_name
#         self.location = location
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
# # Ниже код для проверки классов Person, Company и Employee
#
# ivan = Person('Ivan', 32)
# assert ivan.name == 'Ivan'
# assert ivan.age == 32
# ivan.display_person_info()
#
# zara = Company('Zara', 'Prague')
# assert zara.company_name == 'Zara'
# assert zara.location == 'Prague'
# zara.display_company_info()
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# assert isinstance(emp.personal_data, Person)
# assert isinstance(emp.work, Company)
#
# assert emp.personal_data.name == 'Jessica'
# assert emp.personal_data.age == 28
# emp.personal_data.display_person_info()
#
# assert emp.work.company_name == 'Google'
# assert emp.work.location == 'Atlanta'
# emp.work.display_company_info()
#
# emp2 = Employee('Kolya', 11, 'Facebook', 'Seattle')
# assert isinstance(emp2.personal_data, Person)
# assert isinstance(emp2.work, Company)
#
# assert emp2.personal_data.name == 'Kolya'
# assert emp2.personal_data.age == 11
# emp2.personal_data.display_person_info()
#
# assert emp2.work.company_name == 'Facebook'
# assert emp2.work.location == 'Seattle'
# emp2.work.display_company_info()



# class Task():
#
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         if self.status:
#             print(f'{self.name} (Сделана)')
#         else:
#             print(f'{self.name} (Не сделана)')
#
# class TaskList():
#
#     def __init__(self):
#         self.task = []
#
#     def add_task(self, name):
#         self.task.append(name)
#
#     def remove_task(self, name):
#         self.task.remove(name)
#
# class TaskManager():
#
#     def __init__(self):
#         tack_list = TaskList()
#
#     def mark_done(self, name, description, status=False):
#         pass
#
#
# # Ниже код для проверки классов Task, TaskList и TaskManager
#
# # Создаем список задач
# todo = TaskList()
# assert todo.tasks == []
#
# # Создаем несколько задач и добавляем их в список
# task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
# assert task1.name == 'Стирка'
# assert task1.description == 'Постирать трусы, носки, слюнявчики'
# assert task1.status is False
# task1.display()
#
# todo.add_task(task1)
# assert len(todo.tasks) == 1
#
# task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
# assert task2.name == 'Продукты'
# assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
# assert task2.status is False
#
# todo.add_task(task2)
# assert len(todo.tasks) == 2
#
# # Создаем менеджер задач и показываем список задач
# manager = TaskManager(todo)
# assert isinstance(manager.task_list, TaskList)
# print('-----Список дел-----')
# manager.show_tasks()
#
# # Отмечаем первую задачу выполненной и показываем список задач
# manager.mark_done(task1)
#
# # Проверяем изменился ли статус 2мя способами
# assert task1.status is True
# assert manager.task_list.tasks[0].status is True
#
# print('-----Список дел-----')
# manager.show_tasks()
#
# # Удаляем вторую задачу и показываем список задач
# todo.remove_task(task2)
#
# assert len(todo.tasks) == 1
# assert len(manager.task_list.tasks) == 1
#
# print('-----Список дел-----')
# manager.show_tasks()

