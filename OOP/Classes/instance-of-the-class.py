#!/usr/bin/python3
import random


def main():
    Test1_obj1 = Test1()
    Test1_obj2 = Test1()
    print(Test1_obj1.var, Test1_obj2.var)
    print(Test1_obj1, type(Test1_obj1))
    print(Test1_obj2, type(Test1_obj2))
    # When we call a method on an instance, the instance is passed as the first argument automatically (default implicit behaviour)
    # That's why instance methods are known as "bound" methods, i.e. bound to the instance upon which it is called
    # self is the object in which the method was called
    # Syntax: instance.method(args)
    Test1_obj1.callme()
    Test1_obj2.callme()

    Test2_obj1 = Test2()
    Test2_obj2 = Test2()
    # To access the value of rand_val attribute, we must call dothis() method at first
    Test2_obj1.dothis()
    print(Test2_obj1.rand_val)
    print(Test2_obj1.rand_val)
    Test2_obj1.dothis()
    print(Test2_obj1.rand_val)
    Test2_obj1.dothis()
    print(Test2_obj1.rand_val)
    # Instance values are stored right in the instance (Instances have their own data, instance attributes)


class Test1(object):
    var = 'Hello, this is an attribute of the class'
    def callme(self):
        print("Calling \"callme\" method with instance")
        print(self, type(self))


class Test2(object):
    def dothis(self):
        # Syntax: self.attribute = value
        self.rand_val = random.randint(1, 10) # Setting an instance's attribute

# If the namespace is __main__, then call the function main()
if __name__ == "__main__": main()