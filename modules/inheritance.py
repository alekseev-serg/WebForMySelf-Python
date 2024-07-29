from modules.encapsulation import Person


class Employee(Person):

    company = 'Google'

    def more_info(self):
        print(f'Hello, {self.name}, Age is {self.age}, Company is {self.company}')

