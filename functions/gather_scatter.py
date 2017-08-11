# Variable-Length Argument Tuples
# Functions can take a variable number of arguments. A parameter name that begins with * gathers arguments into a tuple.
# The gather parameter can have any name you like, but args is conventional.
# gather: The operation of assembling a variable-length argument tuple.
def printall(*args):
    print(type(args))
    for x in args:
        print(x, end = ' ')
    print('')
printall(2, '3', 5)
printall(3, (2, "Two"), [3, 5], 7)
# The complement of gather is scatter. If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator.
# scatter: The operation of treating a sequence as a list of arguments.
def divmod(a, b):
    return a // b, a % b
print("Calling the function divmod and storing the returned values within a tuple")
t = divmod(7, 2)
print("The tuple is", (t,)) # If you print a single tuple and no other var/expr/val will be printed, you must but comma at the end % (t,)
# The complement of gather is scatter. If you have a sequence of values (tuple, list, string, range) and you want to pass it to a function as multiple arguments, you can use the * operator.
t = (9, 4)
print("Passing the tuple", t, "to the function divmod and storing the returned values within two variables x and y")
x, y = divmod(*t)
print("The value of x is %d and y is %d" % (x, y))
l = [9, 4]
print("Passing the list", l, "to the function divmod and storing the returned values within two variables x and y")
x, y = divmod(*l)
print("The value of x is %d and y is %d" % (x, y))
def PrintAll(*args): # We can pass any number of arguments and it will gathered within a tuple of values
    print(type(args))
    for x in args:
        print(x, end = ' ')
    print('')
rangeObj = range(1, 11)
PrintAll(*rangeObj) # We passed a sequence of values to the function and it will be scattered (treated as multiple arguments)

def print_func(x, y, z, *args): # *args means that we can pass any number of args (all will be gathered in a tuple)
    print(x, y, z, args, end = '  ')
    for x in args:
        print(x, end = '  ')
    print()
print_func(1, 2, 3)
print_func(1, 2, 3, 4)
print_func(1, 2, 3, 4, 5, 6, 7, 8)
