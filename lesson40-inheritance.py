from modules.inheritance import Person, Employee

person3 = Person('John', 25)
person3.age = 28
person3.print_info()


employee = Employee('Ann', 30)
employee.print_info()
employee.more_info()
