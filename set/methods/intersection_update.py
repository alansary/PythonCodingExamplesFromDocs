# intersection_update()
'''
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
'''
	# Note that: You can pass any number of sets to the intersection_update method
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the first set with the intersection of itself and the second set")
first_set.intersection_update(second_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
print("Again")
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the second set with the intersection of itself and the first set")
second_set.intersection_update(first_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 1, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
first_set.intersection_update(second_set, third_set)
print("Updating the first set with the intersection of itself and second and third sets, the first set now is %r" % first_set)

