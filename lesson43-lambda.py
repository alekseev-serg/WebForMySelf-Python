# def get_square(number):
#     return number ** 2
#
# print(get_square(5))


# get_square = lambda number: number ** 2
# print(get_square(10))


print((lambda number: number ** 2)(5))

l = [1, 2, 3, 4, 5]


def get_double(l):
    return list(map(lambda x: x * 2, l))


print(get_double(l))
