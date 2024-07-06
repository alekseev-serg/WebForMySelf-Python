# while True:
#     print('Hello')

i = 1
while i < 11:
    print(i)
    i += 1

print('hello', 'world', sep='\n')
print('hello', 'world', sep='!')
print('hello', 'world', sep='!', end=' ')
print('hello', 'world', sep='!')

i = 1
while i < 11:
    print(i, end=' ')
    i += 1

print(" ")

s = 'hello world'
for item in s:
    if item == ' ':
        continue
    print(f'"{item}"', end=' ')

print(" ")

for i in 'helloworld':
    if i == ' ':
        break
    print(i, end=' ')
else:
    print("\n No spaces")
