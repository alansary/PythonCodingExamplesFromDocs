 Documentation
	# pydoc3 tuple
'''
Help on class tuple in module builtins:

class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
'''
	# Tuples are immutable, ordered by index, and can hold hetrogeneous data.
	# Important Note: Always enclose tuples within parentheses when using the percent sign to format your string, otherwise, it will substitute
	#		  the value of the tuple and you will get error because of mismatch between the number of arguments and format specifiers.
	# Tuples are iterables as will as sequences of items.
# Use Case: Object that will always be the same size and have the same data in it.
# What really creates a tuple is the comma operator not the parentheses
t1 = 1, 2, 3, 4, 5
print(t1, type(t1))
t2 = (1, 2, 3, 4, 5)
print(t2, type(t2))
t3 = 1,
print(t3, type(t3))
t4 = 1
print(t4, type(t4))
# Creating an empty tuple
empty_tuple = tuple()
print("%r is an empty tuple" % (empty_tuple,))
empty_tuple = ()
print("%r is an empty tuple" % (empty_tuple,))
# Creating a tuple
t = (1, True, "One", 1.4, range(1, 11), list(range(1, 11)), ['x', 'y', 'z'], (1, 2, 3), 'c', {True:1, False:0})
print("%r is a tuple" % (t,))
t = (1,)	# Note the existance of the comma at the end
print("%r is a tuple that contains only one item, %r" % (t, type(t)))
t = 1,		# Note the existance of the comma at the end
print("%r is a tuple that contains only one item, %r" % (t, type(t)))
# Creating a tuple from iterables
test_list = [1, 2, 3]
test_dict = {1:True, 0:False}
test_string = "This is a string"
test_rangeObj = range(1, 11)
test_tuple = (1, 2, 3)
print("%r is a tuple from the list %r" % (tuple(test_list), test_list))
print("%r is a tuple from the dict %r" % (tuple(test_dict), test_dict))
print("%r is a tuple from the string %s" % (tuple(test_string), test_string))
print("%r is a tuple from the range Object %r" % (tuple(test_rangeObj), test_rangeObj))
print("%r is a tuple from the tuple %r" % (tuple(test_tuple), test_tuple))
# The following is an assignment not creation of a tuple
x = 1
print("x = %d which is of type %r" % (x, type(x)))
y, z = 2, 3
print("y = %d and z = %d which are of type %r" % (x, y, type(x)))
x, y, z = 1, 2, 3
print("x = %d, y = %d and z = %d which are of type %r" % (x, y, z, type(x)))
# Accessing the elements of a tuple (Index operator)
test_tuple = (1, 2.5, True, {True:"One", False:"Zero"}, ('x', 'y', 'z'), ['e1', 'e2', 'e3'], tuple(range(1, 6)))
print("Our test tuple is %r" % (test_tuple,))
print("The first element of the tuple is %d" % test_tuple[0])
print("The second element of the tuple is %f" % test_tuple[1])
print("The third element of the tuple is %r" % test_tuple[2])
print("The last element of the tuple is %r" % (test_tuple[len(test_tuple)-1],))
# Tuples and for loops
print("Iterating through the elements of the tuple %r" % (test_tuple,))
counter = 1
for e in test_tuple:
    print("the element number %d is %r" % (counter, e))
    counter += 1
# The len operator
print("The length of the tuple %r is %d" % (test_tuple, len(test_tuple)))
# Tuples and slice operator
print("The items of the tuple %r from index 2 up to but not including index 6 is %r" % (test_tuple, test_tuple[2:6]))
# Tuple Operations
	# Concatenation
t1 = (1, 2, 3)
t2 = ('One', 'Two', 'Three')
print("The first tuple is %r and the second tuple is %r" % (t1, t2))
t3 = t1 + t2
print("The result of concatenation of the first tuple with the second tuple is %r which is of type %r" % (t3, type(t3)))
t4 = t1 + ('A',)
print("The result of concatenation of the first tuple with the tuple ('A',) is %r which is of type %r" % (t4, type(t4)))
t5 = t1 + tuple(['x', 'y', 'z'])
print("The result of concatenation of the first tuple with tuple(['x', 'y', 'z']) is %r which is of type %r" % (t5, type(t5)))
	# Duplication
t1 = (1, 2, 3)
t2 = t1 * 2
print("The first tuple is %r and the second tuple is a duplication of the first tuple which is %r" % (t1, t2))
t3 = (4, 5, 6)
print("The third tuple is %r" % (t3,))
t3 *= 3	# t3 now referes to a new object
print("The third tuple now referes to a new object %r" % (t3,))
# Tuple Comparisons
'''
The relational operators work with tuples and other sequences; Python starts by com‐
paring the first element from each sequence. If they are equal, it goes on to the next
elements, and so on, until it finds elements that differ. Subsequent elements are not
considered (even if they are really big).
'''
t1 = (5, 1, 0)
t2 = (5, 0, 99999999)
print("The first tuple is %r and the second tuple is %r" % (t1, t2))
print("Is %r > %r? %r" % (t1, t2, t1 > t2))
print("Explain! starting by the first item -> 5 == 5, then it goes on to the next items -> 1 > 0 -> True, and subsequent items are not considered")
# Tuples and Functions
t = ('x', 'y', 'z')
x, y, z = t
print("The tuple is %r, x is %s, y is %s and z is %s" % (t, x, y, z))
def return_fun1():
    return 2, 3
t = return_fun1()
print(t, type(t))
def return_fun2():
    return (2, 3)
t = return_fun2()
print(t, type(t))
x, y = return_fun1()
print(x, y, type(x), type(y))
x, y = return_fun2()
print(x, y, type(x), type(y))
def return_fun3():
    return 2,
t = return_fun3()
print(t, type(t))
def return_fun4():
    return 2
t = return_fun4()
print(t, type(t))
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
print("The tuple is", (t,)) # If you print a single tuple and no other var/expr/val will be printed, you must put comma at the end % (t,)
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
# tuples and lists
# You can use tuple assignment in a for loop to traverse a list of tuples, but the tuples must be of the same length
test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)] 	# list of tuples of length three
	# test_list is a list of four three-tuples
print("The list of tuples of length three is %r, traversing the elements:" % (test_list))
x = 0
for e1, e2, e3 in test_list:
    print("The first element in the tuple %r is %d" % (test_list[x], e1))
    print("The second element in the tuple %r is %d" % (test_list[x], e2))
    print("The third element in the tuple %r is %d" % (test_list[x], e3))
    x += 1
# If you combine zip , for and tuple assignment, you get a useful idiom for traversing two (or more) iterables at the same time.
	# zip function
'''
Help on class zip in module builtins:

class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
'''
my_list = [1, 2, 3]
my_dict = {3:"This is the third element", 4:"This is the fourth element", 5:"This is the fifth element"}
my_tuple = (6, 7, 8)
print(zip(my_list, my_dict, my_tuple))
for i in zip(my_list, my_dict, my_tuple):# Results -> [t1, t2, t3], t1 = (e11, e21, e31), t2 = (e12, e22, e32), and t3 = (e13, e23, e33) "Columns"
    print(i, type(i))
iterator = [tuple(my_list), tuple(my_dict), tuple(my_tuple)]
for i in iterator:			 # Results -> [t1, t2, t3], t1 = (e11, e12, e13), t2 = (e21, e22, e23), and t3 = (e31, e32, e33) "Rows"
    print(i, type(i))
print("Using the zip function, we can traverse different sequences at the same time")
counter = 0
for x, y, z in zip(my_list, my_dict, my_tuple):
    print("The element of index %d in the list is %d" % (counter, x))
    print("The element of index %d in the dict is %d" % (counter, y))
    print("The element of index %d in the tuple is %d" % (counter, z))
    counter += 1
print("Using a list of different items, we can traverse a sequence then move on to traverse the next sequence")
counter = 0
for x, y, z in iterator:
    print("The first element in the item %r is %d" % (iterator[counter], x))
    print("The second element in the item %r is %d" % (iterator[counter], y))
    print("The third element in the item %r is %d" % (iterator[counter], z))
    counter += 1
# tuples and dictionaries
my_dict = {1:"This is one", 2:"This is two", 3:"This is three"}
print("The dictionary is", my_dict)
print("The items of the dictionary are", my_dict.items()) # dict.items() is a sequence, interpreted as a list of two tuples [key-value tuples]
for key, value in my_dict.items():
    print(key, value)
# You can use a list of 2-tuples to initialize a new dictionary:
l = [('a', 0), ('c', 2), ('b', 1)]
print("The list of 2-tuples is", l)
print("Initializing a dictionary from a list of 2-tuples, %r" % (l))
d = dict(l)
print("The dictionary is", d)
# Combining dict with zip yields a concise way to create a dictionary:
d = dict(zip('abc', range(101))) # The keys are the elements of the first iterable and the values are the elements of the second iterable
				 # It stops iteration when the shortest iterable is exhausted
print("The dictionary is", d, "which is the result of zipping the elements of the string \'abc\' and the range obj from 0 to 100")
print("Note that: The zip stops iteration when the shortest iterable is exhausted")

