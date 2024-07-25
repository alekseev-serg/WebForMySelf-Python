# print(100 / 10  SyntaxError
# print(1/0) ZeroDivisionError
# print(1 + '123') TypeError
# print(int('Hello World')) ValueError

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Division by zero")

# try:
#     print(1/'1')
# except ZeroDivisionError:
#     print("Division by zero")
# except TypeError:
#     print("Type Error")

# try:
#     print(100/0)
# except Exception:
#     print("Division by zero")
# else:
#     print("Else")
# finally:
#     print("Finally")

while True:
    try:
        num = int(input("Enter a number: "))
        print(100 / num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("That's not an integer!")
