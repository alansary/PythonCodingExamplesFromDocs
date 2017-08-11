#!/usr/bin/env python3
# Polymorphism: Is the practice of using one object of one particular class as if it were another object of another class


def main():
    donald = Duck()
    fido = Dog()
    for obj in (donald, fido):
        print(obj)
        obj.bark()
        obj.fur()
        obj.quack()
        obj.walk()
        print('=' * 20)

    in_the_forest(donald)
    print('=' * 20)
    in_the_pond(fido)


class Common(object):
    def __str__(self): return '{}'.format(self.__class__.__name__)


class Duck(Common):
    def quack(self): print("Quaaaak!")

    def walk(self): print("Walks like a duck.")

    def bark(self): print("The duck cannot bark")

    def fur(self): print("The duck has feathers")


class Dog(Common):
    def bark(self): print("Woof!")

    def fur(self): print("The dog has brown and white fur")

    def walk(self): print("Walks like a dog.")

    def quack(self): print("The dog cannot quack")


# As long as the duck has the methods bark() and fur(), we can pass a duck object because dog is nothing but a reference
# to the passed object
def in_the_forest(dog):
    dog.bark()
    dog.fur()


# As long as the dog has the methods quack() and walk(), we can pass a dog object because bird is nothing but
# a reference to the passed object
def in_the_pond(bird):
    bird.quack()
    bird.walk()

if __name__ == "__main__": main()