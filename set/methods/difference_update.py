# difference_update()
'''
 |  difference_update(...)
 |      Remove all elements of another set from this set.
'''
	# Note that: You can pass any number of sets to the difference_update method
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The difference between the first set and the second set (first set - second set) is %r" % first_set.difference(second_set))
print("Removing all elements of the second set from the first set (difference update the first set from the second set)")
first_set.difference_update(second_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
print("Removing all elements of the second and third sets from the first set (first set = (first set - second set - third set))")
first_set.difference_update(second_set, third_set)
print("The first set now is %r" % first_set)

