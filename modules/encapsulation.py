class Person:
    # name = 'John'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Hello, {self.name}, Age is {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            self.__age = 18
