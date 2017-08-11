class MyClass(object):
    pass

this_obj1 = MyClass()
print(this_obj1)
that_obj1 = MyClass()
print(that_obj1)

class MySecondClass(object):
    var = 10

this_obj2 = MySecondClass()
print(this_obj2)
print(this_obj2.var)
that_obj2 = MySecondClass()
print(that_obj2)
print(that_obj2.var)