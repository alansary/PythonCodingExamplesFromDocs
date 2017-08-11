#!/usr/bin/python3


def main():
    Test1_obj1 = Test1() # Creating an instance of the class Test1
    Test1_obj2 = Test1() # Creating an instance of the class Test1
    # __main__ refers to the namespace (the namespace of the script currently executed)
    # The Hex code at the right is the address in memory where the object is being stored
    print(Test1_obj1, type(Test1_obj1))
    print(Test1_obj2, type(Test1_obj2))
    print("{} is {} ? {}".format(Test1_obj1, Test1_obj2, Test1_obj1 is Test1_obj2))

    Test2_obj1 = Test2()
    Test2_obj2 = Test2()
    print(Test2_obj1, type(Test2_obj1))
    print(Test2_obj2, type(Test2_obj2))
    print("{} is {} ? {}".format(Test2_obj1, Test2_obj2, Test2_obj1 is Test2_obj2))
    # Syntax: object.attribute
    print(Test2_obj1.var) # Accessing the attribute var within the class Test2
    print(Test2_obj2.var)


class Test1(object):
    pass


class Test2(object):
    var = 10
    '''
        Class: a blueprint for an instance
        Instance: a constructed object of the class
        Type: indicates the class the instance belongs to
        Attribute: an object value (object.attribute)
        Method: a "callable attribute/function within a class" defined in the class (object.method(args))
            - Each instance of the class has the same methods (behaviours/functionality) but different attributes(values)
            - Each method is an attribute but the opposite is not True
    '''
if __name__ == "__main__": main()