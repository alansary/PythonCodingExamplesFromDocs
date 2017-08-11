#!/usr/bin/env python3

# Decorators are used to create accessor functions for methods


def main():
    donald = Duck()
    donald.color = 'Yellow'
    print(donald.color)
    # Now the color attribute is under the control of the object
    print(donald.age)
    donald.age = 11 # This calls the setter
    print(donald.age) # This calls the getter (accessor)
    del donald.age # This calls the deleter
    print(donald.age)


class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print("Quaaaak!")

    def walk(self):
        print("Walks like a duck.")

    def get_variables(self):
        return self.variables

    def get_variable(self, key):
        return self.variable.get(key, None)

    def set_variable(self, key, value):
        self.variables[key] = value

    @property
    def color(self): # This is the accessor (getter)
        return self.variables.get('color', None)

    @color.setter
    def color(self, c): # This is the setter
        self.variables['color'] = c

    @color.deleter
    def color(self): # This is the deleter
        del self.variables['color']

    @property
    def age(self):
        return self.variables.get('age', None)

    @age.setter
    def age(self, value):
        self.variables['age'] = value

    @age.deleter
    def age(self):
        del self.variables['age']


if __name__ == "__main__": main()