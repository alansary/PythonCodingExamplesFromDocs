#!/usr/bin/env python3
# The class is the blueprint and any object of the class is an instance of that class
# When calling a method of a class on an instance of the class, this object is passed to this methods
# through the dot operator and self becomes a reference to this object

class Duck:
    def __init__(self, power):
        print("Constructor")
        self._duck_power = power # This creates a local variable that is an attribute of the object (object variable)
        # I named it with an underscore at the beginning to tell myself that this is an attribute that I'm using locally
        # that is, I will access it only through a method not directly

    def quack(self):
        print("Quaaaak")

    def walk(self):
        print("Walks like a duck")

    def my_power(self):
        print("{} {} power is {}".format(self, self.__class__.__name__, self._duck_power))


donald = Duck(100)
donald.quack() # This period is the dot operator (Attribute or Method dereference)
donald.walk()
donald.my_power()


class Employee:
    def __init__(self, name = ''):
        self.name = name
    # Always make your attributes local to the class (only accessed through methods within the class and not accessed directly)
    def print_my_name(self):
        print(self.name)


mohamed = Employee('Mohamed Alansary')
print(mohamed.name) # Accessing an attribute directly will be very hard to track
mohamed.name = 'Mohamed Amr'
print(mohamed.name)


class Best_Practice_Employee:
    def __init__(self, **kwargs):
        self._name = kwargs.get('name', '')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_name(self, name = ''):
        self._name = name

    def get_name(self):
        return self._name


mohamed = Best_Practice_Employee(name = 'Ansary', age = 23)
print(mohamed.get_name())
mohamed.set_name('Mohamed Alansary')
print(mohamed.get_name())
print(mohamed.age)


class Test:
    def __init__(self, **kwargs):
        self.vars = kwargs

    def set_var(self, key, value):
        self.vars[key] = value

    def get_var(self, key):
        return self.vars.get(key, None)

obj = Test()
obj.set_var('name', 'Mohamed Alansary')
obj.set_var('age', 23)
print(obj.get_var('name'))
print(obj.get_var('age'))
print(obj.get_var('weight'))


class fibonacci():
    # __init__ method is a constructor and it gets called when the object is assigned (dander init)
    # __init__ is optional not mandatory

    def __init__(self, x, y): # x and y are passed to the class when creating an object of the class
        # self is a reference to the instantiated object (It is common to call it self, but you can change it)
        self.x = x # Make the value of x for self is the value of the passed x
        self.y = y # This creates initial values for x and y (Declaring variables and initializing them)

    def series_generator(self): # self now has values x and y
        # series_generator is a method (function within a class is called a method)
        # It is a generating function

        while(True):
            yield self.y
            self.x, self.y = self.y, self.x + self.y # Updating the values


f1 = fibonacci(0, 1) # Instantiating (Creating an object of the class)
for element in f1.series_generator():
    if element > 100:
        break
    print(element, end = '  ')
print('')

f2 = fibonacci(13, 21)
for element in f2.series_generator():
    if element > 100:
        break
    print(element, end='  ')


# We can write it like so; however, the first method is considered to be best practices
'''
class fibonacci():
    def series_generator(self, x, y):
        while(True):
            yield y
            x, y = y, x + y
f1 = fibonacci()
for element in f1.series_generator(0, 1):
    if element > 100:
        break
    print(element, end = '  ')
print('')
f2 = fibonacci()
for element in f2.series_generator(13, 21):
    if element > 100:
        break
    print(element, end='  ')
'''


class my_class:
    def __init__(self, kind='fried'): # This constructor is called each time we create an object
        self.kind = kind # self.kind is an object variable (referenced to the object itself)
        # self.kind = kind creates an object variable (encapsulated in the object so that each object can have a different value for kind)

    def whatkind(self):
        return self.kind

print()
my_obj = my_class()
print(my_obj.kind)
print(my_obj.whatkind())
my_obj2 = my_class('egg')
print(my_obj2.whatkind())


class primes():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isprime(self, z):
        if z == 1:
            return False
        else:
            for i in range(2, z):
                if z % i == 0: return False
            return True

    def primes_generator(self):
        for i in range(self.x, self.y):
            if self.isprime(i): yield i
            i += 1

test_object = primes(1, 97)
# test_object = primes(1, 98)
for x in test_object.primes_generator():
    print(x, end = '  ')
print('\n' * 2)


class employee():
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1 # Whenever __init__ is called (object is instantiated) increment the number of employees

    def count(self):
        print("Total number of employees:", self.empCount)

    def emp_data(self):
        print("Name:", self.name, "Salary:", self.salary)

emp1 = employee("Mohamed Alansary", 5000)
emp1.count()
emp1.emp_data()
emp2 = employee("Mahmoud Taha", 4000)
emp2.count()
emp2.emp_data()