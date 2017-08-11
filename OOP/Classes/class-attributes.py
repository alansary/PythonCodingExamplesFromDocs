#!/usr/bin/python3
def main():
    # Printing the value of the class attribute using the class
    print(Test.class_attr)

    print('=' * 50)

    # Instantiating an object obj of the class Test and printing the value of the class attribute using this instance
    # Printing the value of the instance attribute using the instance (we can not use the class)
    obj = Test()
    print(obj.class_attr)
    obj.set_value()
    print(obj.instance_attr)

    print('=' * 50)

    # Changing the value of the class attribute using the class
    # Affects all instances that don't change the value of the attribute so far
    Test.class_attr = 10
    print(Test.class_attr)
    print(obj.class_attr)

    print('=' * 50)

    # Changing the value of the class attribute for a particulat instance, obj, of the class Test
    # This affects only this particular instance
    obj.class_attr = 20
    print(obj.class_attr)
    print(Test.class_attr)

    print('=' * 50)

    # Instantiating another object obj2 of the class Test and printing the class attribute using the instance
    # The class attribute of the instance have the same value as the class attribute of the class itself (default)
    # Changing the value of the class attribute for this particular object
    obj2 = Test()
    print(obj2.class_attr)
    obj2.class_attr = 30
    print(obj2.class_attr)
    print(Test.class_attr)
    print(obj.class_attr)

    print('=' * 50)

    # Changing the value of the class attribute using the class
    # This will affect only the class attribute for the instances
    # that has the same value as the class attribute of the class
    Test.class_attr = 40
    print(Test.class_attr)
    print(obj.class_attr)
    print(obj2.class_attr)

    print('=' * 50)

    # Instantiating another class object, obj3 and printing the value of the class attribute for this object
    # Its class attribute value will be the same as the class attribute of the class (default)
    obj3 = Test()
    print(obj3.class_attr)

    print('=' * 50)

    # Printing the class attribute value for the class and all instantiated objects
    print(Test.class_attr)
    print(obj.class_attr)
    print(obj2.class_attr)
    print(obj3.class_attr)

    print('=' * 50)

    # Deleting the value of the class attribute for the instance obj is permitted since its value doesn't equal to
    # the value of the class attribute of the class
    # Now the value of the class attribute for this instance defaults to the value of class attribute of the class
    del obj.class_attr
    print(obj.class_attr)

    print('=' * 50)

    # We can not delete the value of class attribute for obj3 since it has the same value as the class attribute
    # of the class itself
    try:
        del obj3.class_attr
    except:
        print('AttributeError: class_attr')

    print('=' * 50)

    # Deleting the class attribute using the class itself is permitted and results in deleting the class attribute for
    # all the instances that has the same value of class attribute of the class (default)
    # If we tried to print the value of the class attribute for any instance that doesn't change this value,
    # we will get an error AttributeError: 'Test' object has no attribute 'class_attr'
    del Test.class_attr
    try:
        print(obj3.class_attr)
    except:
        print("AttributeError: 'Test' object has no attribute 'class_attr'")
    try:
        print(Test.class_attr)
    except:
        print("AttributeError: type object 'Test' has no attribute 'class_attr'")

    print('=' * 50)

    # The class attribute of all the instances that change its value will be exists until deleted by those instances
    print(obj2.class_attr)

    print('=' * 50)

    # Instantiating a new object of the class, obj4
    # This new object will not have the deleted class attribute as an attribute
    obj4 = Test()
    try:
        print(obj4.class_attr)
    except:
        print("AttributeError: 'Test' object has no attribute 'class_attr'")

    print('=' * 50)

    # Deleting the class attribute for the final object
    del obj2.class_attr
    try:
        print(obj2.class_attr)
    except:
        print("AttributeError: 'Test' object has no attribute 'class_attr'")

    # Now the class attribute is cleared from the class and all the instances that changed its value and it will
    # not appear in further instantiations

'''
    Class Attributes VS. Instance Attributes
        - Variables defined in the class are class attributes
        - Attributes / variables in the class are accessible through the instance
        - Instance attributes are also accessible by the instance
        - When we use the syntax object.attribute, we're asking python to look up the attribute
            - First in the instance
            - Then in the class
        - Method calls through the instance follow this lookup
'''


class Test(object):
    class_attr = None

    def set_value(self):
        self.instance_attr = 100

if __name__ == "__main__": main()