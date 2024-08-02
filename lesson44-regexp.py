import re

# s = 'Это просто строка текста. А это ещё одна строка текста'
# pattern = 'строка'

# print(s.find(pattern))
#
# print(pattern in s)
#
# import re
#
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('Not Match')
#
#
# match = re.search(pattern, s)
# print(match.end())

# print(re.match(pattern, s))
# print(re.findall(pattern, s))
#
# print(re.split(r'\.', s))

s = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, "~",
А это строка с разными символами "!", "@", "-", "&", "?", "_"
a\\b\tc
test string'''

# pattern = '\w+'
# pattern = r'[эт]'
# pattern = r'[эт]+'
# pattern = r'[а-я]+'
# pattern = r'[а-яё0-9]+'
# pattern = r'[а-яА-Я0-9ё]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\da-]+'
# pattern = r'a\\b\tc'
# pattern = r'^\w+'
pattern = r'\w+$'
print(re.findall(pattern, s, flags=re.IGNORECASE))


# test@mail.com
def mail_validate(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email)


print(mail_validate('test@mail.com'))
print(mail_validate('tes123t@mail'))
print(mail_validate('test@mail.com.ua'))
