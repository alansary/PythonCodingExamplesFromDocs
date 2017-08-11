'''
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
'''
	# sets are unordered collections of unique elements, mutable(unhashable), contain only hashable types and can contain hetrogeneous data types
	# We can call the elements of the set (members/items/keys)
# Creating an empty set
empty_set = set()
print("%r is an empty set" % empty_set)
# Creating a set from an iterable
	# Iterables and contain hashable (immutable) items
test_string = "This is a string"
test_list = [(1, 2, 3), 'x', False, 1, 1.5]
test_tuple = ((1, 2, 2, 3, 'x', True, 1.5), "string", 'x', False, 2.4)
test_rangeObj = range(0, 101, 10)
test_zip = zip(range(1, 101, 1), "Sets", {False:0, True:1, ('x', 'y', 'z'):"Tuple"})
test_dict = {1:True, 0:False}
print("Initializing a set from the string '%s'" % test_string)
test_set = set(test_string)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
print("Initializing a set from the list '%r'" % test_list)
test_set = set(test_list)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
print("Initializing a set from the tuple '%r'" % (test_tuple,))
test_set = set(test_tuple)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
print("Initializing a set from the range object '%r'" % test_rangeObj)
test_set = set(test_rangeObj)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
print("Initializing a set from the zip function '%r'" % test_zip)
test_set = set(test_zip)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
print("Initializing a set from the keys of the dictionary '%r'" % test_dict)
test_set = set(test_dict)
print("The set is %r and its type is %r" % (test_set, type(test_set)))
# Initializing a set using the '{}' notation
test_set = {1, 1.5, "String", (1, 2, 3)}
print("Initializing a set using the '{}' notation, the set is %r" % test_set)
# Using len function
print("The length of this set is %d" % len(test_set))
# using the in operator
print("1.5 in %r? %r" % (test_set, 1.5 in test_set))
print("1.4 in %r? %r" % (test_set, 1.4 in test_set))
# Traversing a set with a for loop
print("The items of the set are:")
for i in test_set:
    print(i, end = ' ')
print()
