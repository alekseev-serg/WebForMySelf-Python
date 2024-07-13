# Модули
import os
import random
import random as r

print(os.getcwd())
print(random.randint(0, 100))
print(r.randint(0, 100))

from random import randint, shuffle

print(randint(0, 100))

l = [1, 2, 3, 4, 5]
shuffle(l)
print(l)

from modules import libs

print(libs.get_length('Hello World'))
print(libs.get_count('Hello World', 'e'))

f = libs.get_count
l1 = libs.get_length
print(f('Hello World', 'H'))
print(l1('Hi!'))