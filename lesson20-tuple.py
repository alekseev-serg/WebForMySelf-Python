tup1 = (1, 2, 3, 4, 5)
print(type(tup1))

# Упаковка кортежа
tup2 = 1, 2, 3, 4, 5
print(tup2)

tup3 = tuple((1, 2, 3, 4, 5))
print(tup3)

tup4 = (1)
tup5 = (1,)

print(type(tup4))
print(type(tup5))

tup6 = tuple('Hello')
print(tup6)
print(tup6[1])

tup7 = tuple('Hello')
tup8 = tuple(' world!')
tup9 = tup7 + tup8
print(tup9)
print(len(tup9))
print(tup9.count('l'))
print(tup9.index('o'))

for i in tup9:
    if i == ' ':
        continue
    print(f"'{i}'", end=' ')

print('\n------------------------------------------------------------------------')
tup10 = (10, 11, 12, 13, 14, [1, 2, 3], 15, 16, ['hello', 'world'], 17, ['!'])
print(tup10, id(tup10))

tup10[5][0] = 0
print(tup10, id(tup10))

tup1 = (1, 2, 3, 4, 5)
x, y, z, q, w = tup1
print(x, y, z, q, w)