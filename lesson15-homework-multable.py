# Написать вывод таблицы умножения в ряд
print('Таблица умножения!')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}\t', end= '')
    print('')
