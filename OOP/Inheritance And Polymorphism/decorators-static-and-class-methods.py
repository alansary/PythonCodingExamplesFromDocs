#!/usr/bin/python3
def main():
    obj = InstanceCounter(10)
    print("The value of the object {} is {}".format(obj, obj.value))
    print("Setting the value (20) to the object {}".format(obj))
    obj.set_val(20)
    print("The value of the object {} is {}".format(obj, obj.get_val()))
    print("The order of instantiation of the object {} is {}".format(obj, obj.get_count()))
    # If we called get_total_count() on the instance it will make no difference in the functionality; however, it
    # will be miss leading (for clarity we will call it on the class not on the instance)
    print("The total number of instantiated objects is {}".format(InstanceCounter.get_total_count()))

    print("=" * 50)

    obj2 = InstanceCounter(30)
    print("The value of the object {} is {}".format(obj2, obj2.value))
    print("Setting the value (40) to the object {}".format(obj2))
    obj2.set_val(40)
    print("The value of the object {} is {}".format(obj2, obj2.get_val()))
    print("The order of instantiation of the object {} is {}".format(obj2, obj2.get_count()))
    print("The total number of instantiated objects is {}".format(InstanceCounter.get_total_count()))

'''
    Decorator: Is a processor (special function) that modifies a function
    Class: Is a library of functionality that is associated with the instances that it produces
        Instance Methods: Are the methods that have the instance (self) as its first argument
            - also called Bound Methods because the instance is bound to the methods
        Class Methods: There are some of the functionality that is directly related to the class itself
                       (dealing with class data / class attributes)
                       (it takes the class as argument and works with the class object)
            - these methods are not bound to the instance
            - Applying the @classmethod decorator to a method, we can tell that method to pass the class automatically
              when called instead of the instance
                - Modifies the default binding that instance methods provide to bind to the class instead of the instance
        Static Methods: Are utility methods (they are not designed to work with the class or the instance) since
                        the instance is not required to use these methods
                        it requires no argument and doesn't work with the class or instance but it still belongs
                        to the class code
            - Applting the @staticmethod decorator to a method, we can tell that method not to pass the class or
              the instance automatically (it has nothing to do with either the class or the instance)
                - Modifies the default binding that instance methods provide to bind to nothing
            - these methods are not bound to the instance
'''


class InstanceCounter(object):
    # count is an attribute that is directly related to the class itself (has nothing to do with the instances)
    # count is a class attribute is miss leading to use it as an instance attribute
    count = 0

    # Instance Method
    def __init__(self, val):
        # in self.filterint(val) we are calling it on the instance; however, the instance is not passed
        self.value = self.filterint(val)
        InstanceCounter.count += 1
        self.count = InstanceCounter.count

    # Static Method
    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    # Instance Method
    def set_val(self, val):
        self.value = val

    # Instance Method
    def get_val(self):
        return self.value

    # Instance Method
    def get_count(self):
        return self.count

    # Class Method
    # Typing cls instead of self doesn't actually affect the functionality of the method
    # @classmethod is a special modifier that converts the method into a class method (function / method decorator)
    @classmethod
    def get_total_count(cls):
        return cls.count

if __name__ == "__main__": main()