def upperLower(s):
    return s.upper() if ' ' in s else s.lower()


print(upperLower('helloworld'))


def hello():
    print('hello')


hello()
hello()
hello()


def hello(name):
    print('Hello,', name)


hello('Bob')
hello('Katty')
hello('John')


def get_sum(a, b):
    print(a + b)


get_sum(1, 2)
get_sum(3, 4)


def getSum(a, b):
    return a + b


print(getSum(3, 5))
