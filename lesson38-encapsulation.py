from modules.encapsulation import Person

person1 = Person('Ivan')
person1.print_info()

person2 = Person('Katy')
person2.print_info()

person3 = Person('John')
# person3.__age = 30
# print(person3.name)
# print(person3._Person__age)
person3.print_info()
# print(person3.get_age())
# person3.set_age(28)
person3.age = 28
person3.print_info()
