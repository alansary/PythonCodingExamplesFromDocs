#!/usr/bin/python3
def main():
    obj = MyClass()
    obj.set_value(12)
    print(obj.get_value())
    obj2 = MyClass()
    obj2.value = 13 # The concept of encapsulation is violated here
    print(obj2.get_value(), obj2.value)

    obj3 = MyInteger()
    print(obj3.get_value())
    obj3.set_value(10)
    print(obj3.get_value())
    obj3.increment_value()
    print(obj3.get_value())
    obj3.decrement_value()
    print(obj3.value)
    obj3.value = 'x' # 'Breaking Encapsulation' results in problems with data integrity
    print(obj3.get_value())
    # obj3.increment_value() # TypeError: Can't convert 'int' object to str implicitly
    # By using set_value() we are able to ensure the integrity of the data
    obj3.set_value(100)
    print(obj3.get_value())
    obj3.set_value('12.3')
    obj3.set_value('x')

'''
    # Encapsulation refers to the safe storage of data (as attributes) in an instance
        # Data should be accessed only through instance methods
        # Data should be validated as correct (depending on the requirements set in class methods)
        # Data should be safe from changes by external processes
    # Breaking Encapsulation
        # Although normally set in a setter method, instance attribute values can be set anywhere
        # Python does not implement data hiding (public and private), as does other languages
'''


# Encapsulating the instance and insuring the integrity of its data by using setters and getters (methods)
class MyClass(object):
    # Taking val as an argument and setting it as an attribute for the instance
    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value


class MyInteger(object):
    # value is a class attribute that is inherited to any instance of that class
    # Case the user get the value before setting it
    value = None
    def set_value(self, val):
        try:
            int(val)
        except ValueError as e:
            print(e)
            return
        except TypeError as e:
            print(e)
            return
        self.value = val

    def get_value(self):
        return self.value

    def increment_value(self):
        self.value += 1

    def decrement_value(self):
        self.value -= 1

if __name__ == "__main__": main()
