s = 'hello, world!'
print(len(s))
print(s.capitalize())
print(s.center(19, '!'))
print(s.count('l'))
print(s.count('l', 0, 3))  # от 0 символа до 3 не включительно
print(s.find('l'))
print(s.find('a'))  # если символ не найден, то -1
print(s.index('o'))

print(s.replace('l', '1'))
print(s.split())

print(s.isdigit())  # строка должна состоять целиком из цифр целиком
print(s.isalpha())  # строка должна состоять целиком из букв целиком без пробелов
print(s.isalnum())  # строка должна состоять из букв и цифр без пробелов и знаков припенания в нижнем регистр
print(s.islower())  # строка должна состоять из символов в нижнем регистре
print(s.isupper())  # строка должна состоять из символов в верхнем регистре
