# symmetric_difference()
'''
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.    
 |      (i.e. all elements that are in exactly one of the sets.)
'''
	# Note that: The symmetric difference can be represented by the '^' symbol
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The symmetric difference between the first set and the second set is %r which is the same as %r" % (first_set.symmetric_difference(second_set), second_set.symmetric_difference(first_set)))
first_set = {1, 2, 3, 4}
second_set = {4, 3, 1, 2}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The symmetric difference between the first set and the second set is %r which is the same as %r which is the same as %r" % (first_set.symmetric_difference(second_set), second_set.symmetric_difference(first_set), first_set ^ second_set))

