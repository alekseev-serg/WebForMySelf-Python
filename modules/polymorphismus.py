from modules.encapsulation import Person


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'Hello, {self.name}, Age is {self.age}, Company is {self.company}')

    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')

