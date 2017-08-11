# sorted()
'''
Help on built-in function sorted in module builtins:

sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
'''
iter_word = "word"
iter_string = "This is a string"
iter_list = [1, 2, 3]
iter_tuple = (4, 5, 6)
iter_rangeObj = range(1, 11)
print(sorted(iter_word, key = None, reverse = False))
print(iter_word)
print(sorted(iter_string, key = None, reverse = False))
print(sorted(iter_string))
print(iter_string)
print(sorted(iter_list, key = None, reverse = False))
print(iter_list)
print(sorted(iter_tuple, key = None, reverse = False))
print(iter_tuple)
print(sorted(iter_rangeObj, key = None, reverse = False))
print(iter_rangeObj)
print(sorted(enumerate(iter_word), key = None, reverse = True))
# Note that enumerate returns an iterator
