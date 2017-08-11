#!/usr/bin/python3
import random


def main():
    my_dog = Dog('Fido')
    print(my_dog.name)
    my_dog.fetch('ball')
    print(my_dog.bread)

    his_dog = Dog('Rover')
    print(his_dog.name)
    his_dog.fetch('paper')
    print(his_dog.bread)


class Animal(object):

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    # If a class doesn't have an __init__ constructor, Python will check its parent class to see if it can find one
    # As soon as it finds one, Python call it and stops looking
    # We can use super() function to call functions in the parent class
    # super() is a built-in function that is designed to relate a class to its super class
    # We are calling Animal __init__() constructor with the Dog object
    # We could use Animal() instead of super() but to make it general (if we changed the class hierarchy), we will
    # use super() instead
    # We now combined the general __init__() functionality with our specific functionality
    # We can leave super without passing any arguments and self (Dog object) will be passed implicitly
    # But it is a best practice to state it explicitly
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.bread = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))

if __name__ == "__main__": main()