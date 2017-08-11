# sum()
'''
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
'''
l = [1, 2, 3]
print("The sum of the numbers in the list %r is %d" % (l, sum(l)))
print("The sum of the numbers in the list %r plus 4 is %d" % (l, sum(l, 4)))
t = (1, 2, 3)
print("The sum of the numbers in the tuple %r is %d" % (t, sum(t)))
print("The sum of the numbers in the tuple %r plus 4 is %d" % (t, sum(t, 4)))
r = range(1, 11)
print("The sum of the numbers in the range object %r from 1 up to but not including 11 is %d" % (r, sum(r)))
print("The sum of the numbers in the range object %r from 1 up to but not including 11 plus 15 is %d" % (r, sum(r, 15)))
d = {1:True, 0:False}
print("The sum of the keys in the dictionary %r is %d" % (d, sum(d)))
print("The sum of the keys in the dictionary %r plus 4 is %d" % (d, sum(d, 4)))

