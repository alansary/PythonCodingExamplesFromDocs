'''
sum(...)
    sum(iterable[, start]) -> value
    
    Return the sum of an iterable of numbers (NOT strings) plus the value
    of parameter 'start' (which defaults to 0).  When the iterable is
    empty, return start.
'''
d = {1:"This is a one", 2:"This is a two", 5:"This is a five"}
print("The dictionary is", d)
print("The summation of the keys of the dictionary is %d" % sum(d))
print("The summaiton of the keys of the dictionary plus 4 is %d" % sum(d, 4))

