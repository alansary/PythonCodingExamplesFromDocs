# intersection()
'''
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      (i.e. all elements that are in both sets.)
'''
	# You can pass any number of sets to the intersection method
	# The intersection can be represented by '&'
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The intersection of the two sets is %r which is the same as %r" % (first_set.intersection(second_set), second_set.intersection(first_set)))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 1, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
print("The intersection between the first set, the second and the third sets is %r which equals %r" % (first_set.intersection(second_set, third_set), first_set & second_set & third_set))

