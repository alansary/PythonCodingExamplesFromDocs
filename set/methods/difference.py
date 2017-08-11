# difference()
'''
 |  difference(...)
 |      Return the difference of two or more sets as a new set.     
 |      (i.e. all elements that are in this set but not the others.)
'''
	# Note that: s1.difference(s2) is not the same as s2.difference(s1)
	# Note that: True == 1 and False == 0
	# Note that: If you repeated a key in the set, it will be saved as one and only one key (members are unique)
	# Note that: We can pass any number of sets to the difference method
	# Note that: The difference can be represented by the '-' symbol
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The difference between the first set and the second set (first set - second set) is %r" % first_set.difference(second_set))
print("The difference between the second set and the first set (second set - first set) is %r" % second_set.difference(first_set))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
print("The difference between the first set and (the second and the third set) (first set - second set - third set) is %r which equals %r" % (first_set.difference(second_set, third_set), first_set - second_set - third_set))

