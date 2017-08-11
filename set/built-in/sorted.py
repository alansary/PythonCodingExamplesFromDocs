# sorted()
'''
Help on built-in function sorted in module builtins:

sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
'''
my_set = {1, 5, 2, 3, 7, 6}
print("The set is %r, the set sorted is %r, and the set sorted and reversed is %r" % (my_set, sorted(my_set), sorted(my_set, reverse = True)))

