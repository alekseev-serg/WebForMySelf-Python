# Методы словаря
product1 = {'title': 'Sony',
            'price': 5.99
            }
product2 = dict(title='iPhone', price=5.99)

# clear - очищает словарь

print(product1.items())
print(product2.keys())
print(product2.values())
print(product2.pop('title'))
# print(product2.pop('title1'))
print(product2.pop('title1', 'NO'))

print(product2.popitem())

print(product1)
print(product1.setdefault('price', 5.99))
print(product1)
print(product1.setdefault('price4', 5.99))
print(product1)
product1.update({'test': 'value'})
product1.update({'price': '250'})
product1.update({'test3': 'value'})
print(product1)

