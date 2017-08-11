# union()
'''
 |  union(...)
 |      Return the union of sets as a new set.     
 |      (i.e. all elements that are in either set.)
'''
	# Note that: You can pass any number of sets to the union method
	# Note that: The union can be represented by the '|' symbol
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The union of the first set with the second set is %r" % first_set.union(second_set))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
print("The Union of the first set, second set and third set is %r which equals %r" % (first_set.union(second_set, third_set), first_set | second_set | third_set))

