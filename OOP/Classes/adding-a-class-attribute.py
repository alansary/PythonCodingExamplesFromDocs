#!/usr/bin/python3
def main():
    # Instantiating an object of the class
    obj1 = TestClass()
    # Setting a new class attribute and initializing it with the value of 10
    TestClass.new_class_attribute = 10
    # Accessing this class attribute through the class
    print(TestClass.new_class_attribute)
    # Accessing this class attribute through the previously instantiated object
    print(obj1.new_class_attribute)

    print('=' * 50)

    # Some experiments
    obj1.new_class_attribute = 20
    print(obj1.new_class_attribute)
    print(TestClass.new_class_attribute)
    TestClass.new_class_attribute = 30
    print(obj1.new_class_attribute)
    print(TestClass.new_class_attribute)


class TestClass(object):
    pass

if __name__ == "__main__": main()