"""
Дан список слов. Составьте из него список слов парадигмов. Попробуйте это сделать двумя способами:
произвольное решение и решение в одну строчку.

Дан список со строками, часть из которых являются палиндромами. Составить новый список строк-палиндромов

"""

words = ['мадам', 'топот', 'тест', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']

new_words = []
print(words[0][::-1])
for item in words:
    if item == item[::-1]:
        new_words.append(item)
print(new_words)

print([item for item in words if item == item[::-1]])

new_my_str = []
for i in my_str:
    if i.replace(' ', '').lower() == i.replace(' ', '').lower()[::-1]:
        new_my_str.append(i)

print([i for i in my_str if i.replace(' ', '').lower() == i.replace(' ', '').lower()[::-1]])

tire = '-'
new_string = tire.join(words)
print(new_string)

intList = list(range(1, 11))
print(intList)
s = '-'.join(map(str, intList))
print(s)
