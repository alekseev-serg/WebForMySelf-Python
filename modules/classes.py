class Person:
    # name = 'John'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print(f'Hello, {self.name}, Age is {self.age}')
