class A:
    property1 = 'Property 1'
    property2 = 'Property 2'

    name = 'guest'

    def say_hello(self, name=''):
        if name:
            return f'Hello {name}!'
        else:
            return f'Hi, {self.name}'


a = A()
b = A()
print(a.say_hello('John'))
print(b.say_hello('Mark'))
print(b.say_hello())
