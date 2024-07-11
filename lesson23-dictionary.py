# Словари
d = {}
print(type(d))
print('---------------------------------------------')
product1 = {'title': 'Sony',
            'price': 5.99
            }
print(product1)
print('---------------------------------------------')
product2 = dict(title='iPhone', price=5.99)
print(product2)
print('---------------------------------------------')
users = [
    ['bob@gmail.com', 'Bob'],
    ['alice@gmail.com', 'Alice'],
    ['serg@gmail.com', 'Serg'],
]
print(users)
d_users = dict(users)
print(d_users)
print('---------------------------------------------')

mails = (
    ('bob@gmail.com', 'Bob'),
    ('alice@gmail.com', 'Alice'),
    ('serg@gmail.com', 'Serg'),
)
t_mails = dict(mails)
print(t_mails)
print('---------------------------------------------')

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product3)

nums = {i: i + 1 for i in range(10)}
print(nums)

print('---------------------------------------------')
product1 = {'title': 'Sony',
            'price': 5.99
            }
product2 = dict(title='iPhone', price=5.99)
print(product1['price'])
print(product2['title'])
print(product1.get('price'))
print(product1.get('prce'))
print('---------------------------------------------')

for key in product1:
    print(key)
    print(product1[key])
    print(f'{key}: {product1[key]}')

print('---------------------------------------------')
for key, value in product1.items():
    print(f'{key}: {value}')

print('---------------------------------------------')
products = [
    {'title': 'Sony', 'price': 5.99},
    {'title': 'iPhone', 'price': 7},
    {'title': 'Samsung', 'price': 9},
]

for product in products:
    print(product['title'], product['price'])