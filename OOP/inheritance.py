#!/usr/bin/env python3
# One class inherits the properties of another class
# The child class (subclass) inherits from the parent class (base class or super class)


def main():
    my_duck = Duck()
    my_duck.talk()
    my_duck.walk()
    my_duck.clothes()
    my_duck.quack()
    my_duck.set_variable('color', 'yellow')
    print(my_duck.get_variable('color'))
    print(my_duck)
    fido = Dog()
    fido.talk()
    fido.walk()
    fido.clothes()
    print(fido)


# Base class
class Animal(object):
    def talk(self): print("I have something to say!")

    def walk(self): print('Hey! I''m walkin'' here!')

    def clothes(self): print("I have nice clothes")

    def __str__(self):
        return '{}'.format(self.__class__.__name__)


class Duck(Animal):
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_variable(self, key, value):
        self.variables[key] = value

    def get_variable(self, key):
        return self.variables.get(key, None)

    def quack(self): print("Quaaaak!")

    def walk(self): print("Walks like a duck.") # Overrides walk in the base class

    def clothes(self):
        # Incorporating the one from its parent
        super().clothes() # This super built-in function accesses the parent class and makes a call to the method clothes() on this object
        print("Yeeeeeeeah! new clothes!")


class Dog(Animal):
    pass

if __name__ == "__main__": main()