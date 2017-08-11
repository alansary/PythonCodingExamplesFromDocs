# Documentation
	# pydoc3 list
'''
dir(list)
help(list.method)
help(list)

Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
'''
	# Lists are mutable, indexed, can contain hetrogeneous data types.
	# Lists are iterables (we iterate through the items of the list).
	# Lists are sequences of items (they are ordered by indices).
    # We can only assign an iterable to a slice
    # Slicing over distinct elements force us to assign to an iterable of length equals the same number of elements
    # or making use of the zip operator with comprehension
# List and while loops
i = 0
l = []
while i < 10:
    l.append(i)
    i += 1
print(l)
# List from Iterable
my_list = list()
print("This is an empty list", my_list)
my_tuple = (1, 2, 3, 4, 5)
print("The tuple is", my_tuple)
my_list = list(my_tuple)
print("The list now is", my_list)
my_dict = {"One":1, "Two":2, "Three":3}
print("The dictionary is", my_dict)
my_list = list(my_dict)
print("The list now is", my_list)
new_list = [1, "two"]
print("The new list is", new_list)
my_list = new_list
print("The list now is", my_list)
my_list = list()
print("The list now is", my_list)
string = "This is a string"
print("The string is", string)
my_list = list(string)
print("The list containing the characters of the string is", my_list)
new_list = list(range(101, 201, 2))
print("The list is %r" % new_list)
# Creating an empty list
empty_list = list()
print("%r is an empty list" % empty_list)
empty_list = []
print("%r is an empty list" % empty_list)
# Assigning a list to a variable
shopping_list = ['shoes', 'socks', 'T-shirt']
print("Shopping list: %r" % shopping_list)
hetro_list = [1, "One", True, 1.0, (1,), {"One":1}, [1]]
print("A sample hetrogeneous list: %r" % hetro_list)
# Lists and the index operator
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is: %r" % num_list)
print("The list is: %r" % num_list[::])
print("The list reversed is: %r" % num_list[::-1])
print("The first three elements of the list are: %r" % num_list[0:3])
print("The last three elements of the list are: %r" % num_list[-1:-4:-1])
print("The odd numbers are: %r" % num_list[::2])
print("The even numbers are: %r" % num_list[1::2])
l = [[1, [2, "two"], 3], [4, 5, [6, "six"]], [[7, "seven"], 8, 9]]
print("%r is  a test list" % l)
print("%r, %r, and %r" % (l[0][1][1], l[1][2][0], l[1][2][1]), "are elements within the list")
# Assigning a slice of the list (Lists and Slicing)
        # string[start:[end:step-size]] or string[start:end[:step-size]] or string[:] or string[[start]:end:step-size] or
        # string[[start]:end[:step-size]] where, the default step-size is 1, the default start is 0, and the default end
        # is len(string)
        # Slice the string from the start up to but not including the end with a step-size of step-size
        # We can use negative indices to traverse the characters of the string from the end
print("Changing all odd numbers with the character \"O\"")
num_list[::2] = "O" * 5
print("The modified list is: %r" % num_list)
print("Changing all even numbers with the character \"E\"")
num_list[1::2] = ["E"] * 5
print("The modified list is: %r" % num_list)
# If the slice slices distinct elements from the list and we don't now how many elements are in there we can use
# the len operator or making use of the zip function and list comprehension as follows
num_list[1::2] = [x[0] for x in zip(range(200, 300, 3), num_list[1::2])]
print(num_list)
# Note that we can use any kind of comprehension
# The len operator
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is: %r and its length is %d" % (num_list, len(num_list)))
# Note that it assigns element by element
# Lists with for Loops
        # Traversing the elements of a list (Iterating through the elements of a list)
hetro_list = [1, "One", True, 1.0, (1,), {"One":1}, [1]]
print("Iterating through the elements of the list %r" % hetro_list)
for element in hetro_list:
    print(element, '\t', end = '')
print('')
list_of_lists = [['l11', 'l12'], ['l21', 'l22', 'l23'], ['l31', 'l32', 'l33', 'l34', 'l35']]
print("Iterating through the basic elements of a list of lists %r" % list_of_lists)
counter = 0
for x in list_of_lists:
    print("\nThe element number %d is the list %r, it contains the elements:" % (counter + 1, x))
    counter += 1
    for y in x:
        print(y, ' ', end = '')
print('')
list_of_tuples = [('l11', 'l12'), ('l21', 'l22', 'l23'), ('l31', 'l32', 'l33', 'l34', 'l35')]
counter = 0
print("Iterating through the basic elements of a list of tuples %r" % list_of_tuples)
for x in list_of_tuples:
    print("\nThe element number %d is the tuple %r, it contains the elements:" % (counter + 1, x))
    counter += 1
    for y in x:
        print(y, ' ', end = '')
print('')
list_of_dicts = [{'l11':11, 'l12':12, 'l13':13, 'l14':14, 'l15':15}, {'l21':True, 'l22':False}, {0:"Octal", 7:"Octal", 8:'Not Octal'}]
print("Iterating through the basic elements of a list of dicts %r" % list_of_dicts)
counter = 0
for x in list_of_dicts:
    print("\nThe element number %d is the dict %r, it contains the following key-value pairs:" % (counter + 1, x))
    counter += 1
    for y in x:
        print("%s:%s" % (y, x[y]), ' ', end = '')
print('')
print('')
# The concatenation Operator (Operator OverLoading)
        # The '+' sign referes to the concatenation operator when it is used with lists
                # In general: list1 + list2 results a new list3 which is nothing but list1 concatenated with list2

list1 = ['e1', 'e2', 'e3']
list2 = [1, 2, 3, 4, 5]
print("The first list is %r and the second is %r" % (list1, list2))
list3 = list1 + list2
print("The third list is %r which is the concatenation between the two lists %r and %r" % (list3, list1, list2))
print("Appending an extra element to this list by using concatenation")
list4 = list3 + ['Extra Element']
print("The new list is %r" % list4)
# The Duplication Operator (Operator OverLoading)
        # The '*' sign referes to the duplication operator when it is used with lists
        # In general: list * int results a new list which is nothing but a duplication of the list int times
test_list = [1, 'One', (1, 2, 3), ['x', 'y', 'z'], 'c', {1:True, 0:False}, True, False]
print("The original list is %r" % test_list)
new_list = test_list * 3
print("The original list duplicated three times is %r" % new_list)
# lists are mutable (We can change them, and assign a slice or make a modification to a list in place)
test_list = ['computer', 'mouse', 'keyboard', 'pad', 'screen']
print("The list is %r" % test_list)
print("Changing the first element '%s' to '%s'" % (test_list[0], 'labtop'))
test_list[0] = 'labtop'
print("The modified list is %r" % test_list)
print("Changing a slice of this list")
test_list[1:3] = ['USB mouse', 'USB keyboard']
print("The modified list is %r" % test_list)
print("Appending elements to the end of the list, we have:")
test_list += ['scanner', 'printer']
print("The modified list is %r" % test_list)
# Lists and in operator
Accessories = ['keyboard', 'mouse', 'pad']
shopping_list = ['Computer', Accessories]
print("Accessories are %r" % Accessories)
print("Shopping list is %r" % (shopping_list))
print("Is %r in %r? %r" % (Accessories, shopping_list, Accessories in shopping_list))
print("Is '%s' in %r? %r" % ('Computer', shopping_list, 'Computer' in shopping_list))
print("Is '%s' in %r? %r" % ('computer', shopping_list, 'computer' in shopping_list))
# Looping with indices using the range built-in function
shopping_list = ['shoes', 'socks', 't-shirts']
print("The shopping list is %r" % (shopping_list))
for i in range(len(shopping_list)):
    print("The element %s is of index %d" % (shopping_list[i], i))

# Lists and Aliasing
    #The association of a variable with an object is called a reference. In this example,
    #there are two references to the same object.
    #An object with more than one reference has more than one name, so we say that the
    #object is aliased.
    #If the aliased object is mutable, changes made with one alias affect the other.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("The first list is %r and the second list is %r" % (list1, list2))
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
print("Modifing the list %r and checking the list %r" % (list1, list2))
list1[::] = [0, 1, 2]
print("Now, the first list is %r but the second list %r still the same" % (list1, list2))
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
	# Aliasing Case
list1 = [1, 2, 3]
list2 = list1
print("The second list %r is assigned the value of the first list %r" % (list2, list1))
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Alisasing\")" % (list1, list2, list1 is list2))
if list1 is list2:
    print("The object [1, 2, 3] have more than one reference (more than one name), this object is aliased")
    print("The aliased object is a list (mutable), so changes made with one alias affect the other")
print("Modifing the elements of the first list %r and checking the second list %r" % (list1, list2))
list1[::] = [0, 1, 2]
print("Now, the first list is %r and the second list is %r" % (list1, list2))
print("Modifing the elements of the second list %r and checking the first list %r" % (list1, list2))
list2[0] = 5
print("Now, the second list is %r and the first list is %r" % (list2, list1))
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
print("Assigning the first list %r to entirely new list and checking the second list")
list1 = [7, 8, 9]
print("The first list is assigned to a new object which is %r" % list1)
print("The second list still assigned to the object %r" % list2)
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
print("Assigning the second list %r to entirely new list and checking the first list")
list2 = [7, 8, 9]
print("The second list is assigned to a new object which is %r" % list2)
print("The first list still assigned to the object %r" % list1)
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
	# Avoid aliasing by using the slice operator
print("To avoid this situation, we can use the slice operator to assign the object of one list to the other without aliasing")
list1 = [1, 2, 3]
list2 = list1[::]
print("The first list is %r and the second list is %r" % (list1, list2))
print("Is %r == %r? %r (They are equivalent)" % (list1, list2, list1 == list2))
print("Is %r is %r? %r (They are identical \"Aliasing\")" % (list1, list2, list1 is list2))
# Added
test_list = [1, 2, 3]
print("The list is {}".format(test_list)) # Assigning to a slice the range object range(100)
test_list[1:] = range(100)
print("The list now is {}".format(test_list))
for i in test_list[27:43:3]: print(i, end = '  ')
test_list = [1, 2, 3, 4, 5, 6]
print(test_list)
test_list[0:5] = [3]
print()
print(test_list)
test_list[0:5] = 'a'
print(test_list)
test_list[0:5] = 3,
print(test_list)
test_list[0:5] = [3]
print(test_list)
test_list[0:5] = [[3]]
print(test_list)
test_list[0:5] = (2,)
print(test_list)
test_list[0:5] = [(2,)]
print(test_list)
test_list[0:4] = (2, 3)
print(test_list)
