l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

print(len(l))

print(l[3])
print(l[4][0])
print(l[-1])
print(l[0:4])
l[2] = 5
print(l)
l.append(7)
print(l)
l1 = [1, 2, 3]
l.extend(l1)
print(l)

l2 = ['hello', 'world']
l += l2
print(l)

l.insert(1, 4)
print(l)

l.remove('world')
print(l)

item = l.pop()
print(item, l)
print(l.pop(1))
print(l)

print(l.index(7))

print(l.count('hello'))

numbers = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
print('-----------------------------')
print(sorted(numbers))

words = ['hello', 'world', 'hi', 'apple', 'computer']
words.sort()
print(words)

