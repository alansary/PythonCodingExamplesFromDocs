# sum()
'''
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
'''
my_set = {2, 7, 3, 5, 1, 0}
print("The set is %r, its sum is %d, and its sum plus 4 is %d" % (my_set, sum(my_set), sum(my_set, 4)))

