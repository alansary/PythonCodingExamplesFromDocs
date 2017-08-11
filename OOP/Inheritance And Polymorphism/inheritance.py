#!/usr/bin/python3
def main():
    dt = Date()
    print(dt.get_date())
    td = Time()
    print(td.get_date())
    print(td.get_time())

    print('=' * 100)

    fido = Dog('Fido') # Calling Animal __init__ with a Dog instance
    print(fido.name)
    fido.eat('dog food')
    fido.fetch('ball')

    rover = Dog('Rover')
    print(rover.name)
    rover.eat('banana')
    rover.fetch('papaer')

    fluffy = Cat('Fluffy')
    print(fluffy.name)
    fluffy.eat('mango')
    fluffy.swatstring()



# object is a built-in class provided by python, this class has the following private/magic attributes
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
class Date(object): # Inherits from the 'object' class
    def get_date(self):
        return '2014-10-13'


# object.attribute lookup hierarchy
    # The instance
    # The class
    # Any class from which this class inherits
# An inheriting class VS. An inherited class
    # Child class           Parent class
    # Derived class         Base class
    # subclass              Superclass
class Time(Date): # Inherits from the 'Date' class
    def get_time(self):
        return '08:13:07'


'''
    Examples
'''


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{} is eating {}'.format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('{} goes after the {}!'.format(self.name, thing))


class Cat(Animal):
    def swatstring(self):
        print('{} shreds the string!'.format(self.name))

'''
    INHERITANCE HIERARCHY
        - Classes can be organized into an inheritance hierarchy
        - A child class can access the attributes of all parent (grandparent, etc.) classes
        - Inheritance promotes code collaboration and reuse
        - "No code should appear twice"
        - Become DRY (Don't Repeat Yourself) and never be WET (We Enjoy Typing / Writing Everything Twice)
'''

if __name__ == "__main__": main()