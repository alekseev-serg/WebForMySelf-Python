def get_sum(a, b, c=0, d=5):
    return a + b + c + d


print(get_sum(1, 2, 3, 4))
print(get_sum(1, 2))
print(get_sum(1, 2, d=9))


def get_args(*args):
    return sum(args)


print(get_args(1, 2, 3, 4, 5, 6))


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3, d=4)


def functest(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


functest(1, 2, 3, 4, b='test', c='hi')
