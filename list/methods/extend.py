# extend()
'''
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
'''
	# lists, dicts, tuples, strings, and range objects are iterables.
my_list = [1, 2, 3]
print("The list is %r" % my_list)
my_tuple = (4, 5, 6)
print("Extending the list %r with the tuple %r" % (my_list, my_tuple))
my_list.extend(my_tuple)
print(my_list)
my_new_list = [7, 8, 9]
print("Extending the list %r with the list %r" % (my_list, my_new_list))
my_list.extend(my_new_list)
print(my_list)
my_dict = {True:1, 1.5:"Float"}
print("Extending the list %r with the keys of the dict %r" % (my_list, my_dict))
my_list.extend(my_dict)
print(my_list)
string = "This is a string"
print("Extending the list %r with the characters of the string %s" % (my_list, string))
my_list.extend(string)
print(my_list)
obj = range(1, 11)
print("Extending the list %r with the range object %r" % (my_list, obj))
my_list.extend(obj)
print(my_list)

