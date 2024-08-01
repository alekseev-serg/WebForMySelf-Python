# def hello():
#     return 'Hello i am func hello!'
#
#
# def super_func(func):
#     print("Hello i am super func")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrapper():
#         print('Code before execution')
#         func()
#         print('Code after execution')
#
#     return wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello Test function')
#
#
# func_test()


def make_title(fn):
    def wrapper():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title

    return wrapper


@make_title
def hi():
    return 'hello, world!'


print(hi())
