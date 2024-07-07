x = 10
print(x, id(x))
x = x + 1
print(x, id(x))
x = x + 1
print(x, id(x))

s = 'hello world'
print(s, id(s))
s += '!'
print(s, id(s))

l = [1, 2, 3]
print(l, id(l))
l.append(4)
print(l, id(l))

x = 10
y = x
print(x, id(x))
print(y, id(y))

x = 15
print(x, id(x))
print(y, id(y))

l1 = [1, 2, 3]
l2 = l1
print(l1, id(l1))
print(l2, id(l2))
l1.append(4)
print(l1, id(l1))
print(l2, id(l2))

l3 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))
print(l3, id(l3))

x = 10
print(x, id(x))
del x
print(x, id(x))
