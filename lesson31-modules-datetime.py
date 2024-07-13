# Datetime
import locale
from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print('-------------------------------------')
from datetime import datetime

now1 = datetime.now()
now2 = datetime.today()

print(now1)
print(now2)
print(now1.year)
print(now1.month)
print(now1.day)
print(now1.weekday())
print(now1.hour)
print(now1.minute)
print(now1.second)
print(now1.microsecond)

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс', ]
print(days[now1.weekday()])

print('-------------------------------------')

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

now = datetime.now()
print(now)
print(now.strftime('%a'))
print(now.strftime('%A'))

print(f'Date: {now.strftime("%d/%b/%Y")}')
print(f'Time: {now.strftime("%H:%M:%S")}')

print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))

print('-------------------------------------')

from datetime import timedelta
now = datetime.now()
print(now.strftime('%c'))
now_delta = now + timedelta(days=1, hours=2, minutes=10)
print(now_delta.strftime('%c'))