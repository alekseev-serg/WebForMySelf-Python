s = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple', 'orange', 'banana'}
print(type(s))
print(s)

s2 = set('hello')
print(s2)

s3 = {i for i in range(10)}
print(s3)

s4 = {5, 4, 1, 2, 7, 9}
print(s4)

s5 = set()
print(type(s5))

nums = [1, 2, 3, 4, 1, 2, 3, 4, 5]
nums2 = set(nums)
print(nums)
print(nums2)

s6 = set('abracadabra')
s7 = set('alacazam')
print(s6, s7, sep='\n')

s8 = s6 - s7  # Вычитание множества
print(s8)

s9 = s6 | s7  # Объединение множества
print(s9)

s10 = s6 & s7  # Пересечение множества
print(s10)

s11 = s6 ^ s7  # множества из элементов, попадут буквы a и b. Получаем все буквы кроме дублей.
print(s11)

s = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple', 'orange', 'banana'}


s2 = s.copy()
print(s, id(s))
print(s2, id(s2))

s.add('lemon')
print(s)

s.remove('banana')
print(s)

s.discard('banana2')
print(s)

if 'apple' in s:
    print('OK')

s.clear()
print(s)

s = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple', 'orange', 'banana'}

a = frozenset('apple')
print(a)

for i in s:
    print(i)