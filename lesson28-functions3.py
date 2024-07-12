def functest(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


def get_sum(a, b):
    """
    Возвращает сумму аргументов a и b.


    :param a: integer
    :param b: integer
    :return: sum of two integers
    """
    return a + b


print(get_sum(1, 2))

c = 5  # глобальная


def func():
    c = 10  # локальная
    c += 1
    print(c)


print(c)
func()
print(c)


def func_global():
    global c
    c += 1
    print(c)


print('---------------------')
print(c)
func_global()
print(c)

print('----------------------------')

l = [1, '2', 3, 4, 5]


def func_len(l):
    return [i * 2 for i in l]


print(func_len(l))
print('----------------------------')


def func_len2(l):
    def get_mult(x):
        return int(x) * 2

    return [get_mult(i) for i in l]


print(func_len2(l))
print('----------------------------')

list_number = [1, '2', 3, 4, 5]
list_number_too = [1, 2, 3, 4, 5]


def func_len3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2

    return [get_mult(i) for i in l if get_mult(i)]


print(func_len3(list_number))
print(func_len3(list_number_too))
print('----------------------------')


def func_len4(l):
    def get_mult(x):
        return x * 2

    return list(map(get_mult, l))


print(func_len4(list_number))
