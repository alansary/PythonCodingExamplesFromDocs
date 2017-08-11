# index()
'''
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
'''
	# Note that: index takes value as a parameter not sub-list (not sub like strings)
my_list = ['a', 'b', 'c', 'a', 'b']
print("The list is %r" % my_list)
print("The index of 'b' from the start to the end is %d" % my_list.index('b', 0, len(my_list)))
print("The index of 'b' from index 2 to the end is %d" % my_list.index('b', 2, len(my_list)))
print("Confirmation: my_list[%d] == my_list[%d]? %r" % (1, 4, my_list[my_list.index('b', 0, len(my_list))] == my_list[my_list.index('b', 2, len(my_list))]))
my_list = list(range(1, 101, 2))
print("The list is %r" % my_list)
print("The index of 75 start searching from the index 10 to the end is %d" % my_list.index(75, 10, -1))
print("The value of my_list[my_list.index(75, 10, -1)] is %d" % my_list[my_list.index(75, 10, -1)])
print("Is 16 in %r? %r" % (my_list, 16 in my_list))
if 16 in my_list:
    print("The index of 16 is %d" % my_list.index(16))
else:
    print("16 is not found in the list %r" % my_list)
print("Handling the error with try and except:")
try:
    my_list.index(16)
    print("The index of 16 is %d" % my_list.index(16))
except:
    print("16 is not found in the list %r" % my_list)
print("If you don't handle the error, index will raise a ValueError:")
print("The index of 16 in the list %r is %r" % (my_list, my_list.index(16)))
