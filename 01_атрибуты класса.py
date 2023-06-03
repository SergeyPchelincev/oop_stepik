
class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True



words = input('Введите произвольное количество слов в одну строку, разделенных пробелом: ', )

list_words = words.split(' ')

for word in list_words:
    word_lower = word.lower()
    attr_class = getattr(Person, word_lower, 'Attribute not found')
    if attr_class != 'Attribute not found':
        print('%s-YES' %word)
    else:
        print('%s-NO' %word)

