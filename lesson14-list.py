l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(type(l))
print(l)

l2 = list('Hello')
print(l2)

l3 = list((1, 2, 3))
print(l3)

l4 = [i for i in 'hello']
print(l4)

l5 = [i*2 for i in 'hello world' if i not in [' ', 'e', 'o']]
print(l5)

print(list(range(10)))
l6 = list(range(0, 11, 2))
print(l6)

for i in range(1, 4):
    print(f'Внешний цикл #{i}')
    for j in range(1, 4):
        print(f'\tВнутренний цикл #{j}')