#!/usr/bin/python3
def main():
    # We don't care what type of Animal we have, we just call show_affection() on it and we trust the interface
    # contract that is that we know that every Animal will implement show_affection() to do the right thing
    # when we call it
    # The two classes Cat and Dog have the same interface (same method name and passed args) for the method
    # show_affection(), we can call this method show_affection() on both objects as follows:
    for animal in (Cat('Fluffy'), Dog('Fido'), Dog('Rover'), Cat('Precious')):
        animal.show_affection()

'''
    POLYMORPHISM ("MANY SHAPES")
        - Two classes with same inference (i.e., method name and passed args) (Common Interface)
        - The methods are often different, but conceptually similar
        - We can call the same method on either type of object
        - Conceptual connection and an identical interface between two objects
        - Allows for expressiveness in design: we can say that this group or related classes implement the same action
    DUCK TYPING (Handle Errors Using Exception Handling)
        - Comes from "If it walks like a duck and quacks like a duck, it must be a duck"
        - We will try to do the thing that we expect this object to be able to do rather than to check to see
          whether it is possible
        refers to reading an object's attributes to decide whether it is of a proper type, rather than checking the
        type itself
    EXAMPLES
        The 'len' operator is translated to a method called  __len__()
        The 'in' operator is translated to a method called __contains__()
        The concatenation operator '+' is translated to a method called __add__()
            - All types that which we can use these operators with are implementing these methods in its class
            - len(str/list/tuple/set/dict), element in str/list/tuple/set/dict, str/list/tuple + str/list/tuple
            - These methods are all POLYMORPHIC
'''


class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{} eats {}'.format(self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))

    def show_affection(self):
        print('{} wags tail'.format(self.name))


class Cat(Animal):

    def swatstring(self):
        print('{} shreds the string'.format(self.name))

    def show_affection(self):
        print('{} purrs'.format(self.name))

if __name__ == "__main__": main()