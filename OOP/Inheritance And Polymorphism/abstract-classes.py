#!/usr/bin/python3
import abc
# The abc module provides facilities for creating abstract base classes which are classes that are not designed to
# be instantiated but only to be subclassed (We only inherit from this class and we don't instantiate an object from it)


def main():
    obj = MyClass()
    print(obj)
    print(MyClass.mro())
    obj.set_val(10)
    print(obj.get_val())
    print(type(SetterGetter))
    print(type(MyClass))
    print(issubclass(MyClass, SetterGetter))
    print(MyClass.mro())

    print("=" * 50)

    obj2 = MyFalseClass()
    print(obj2)
    print(MyFalseClass.mro())
    obj2.set_false_value(20)
    print(obj2.get_value())

'''
    ABSTRACT BASE CLASSES
        - An abstract class is a kind of "model" for other classes to be defined. It is not designed to construct
          instances, but can be subclassed by regular classes (blueprints for how subclasses should be designed)
        - Abstract classes can define an interface, or methods that must be implemented by its subclasses
        - One way to create an abstract base class is to make use of __metaclass__ which is basically a class that
          can define other classes
            abstractmethod(funcobj)
                A decorator indicating abstract methods.

                Requires that the metaclass is ABCMeta or derived from it.  A
                class that has a metaclass derived from ABCMeta cannot be
                instantiated unless all of its abstract methods are overridden.
                The abstract methods can be called using any of the normal
                'super' call mechanisms.

                Usage:

                    class C(metaclass=ABCMeta):
                        @abstractmethod
                        def my_abstract_method(self, ...):
                            ...
        - If we omit or change the interface of any of the methods defined in the abc in the subclass we will get an error
            TypeError: Can't instantiate abstract class MyFalseClass with abstract methods set_value
'''


# Abstract Base Class (is considered to be a contract)
class SetterGetter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_val(self, input):
        """Set a value in the instance."""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from the instance."""
        return


# Subclass of the previously defined Abstract Base Class
class MyClass(SetterGetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


class GetterSetter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_value(self, input):
        """Set a value in the instance."""
        return

    @abc.abstractmethod
    def get_value(self):
        """Get and return a value from the instance"""
        return

# We violated the contract of the abstract base class -> Error
class MyFalseClass(GetterSetter):

    def set_false_value(self, input):
        self.val = input

    def get_value(self):
        return self.val

if __name__ == "__main__": main()