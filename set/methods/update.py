# update()
'''
 |  update(...)
 |      Update a set with the union of itself and others.
'''
	# For cosistency, we prefered to name it update() instead of union_update()
	# Note that: You can pass any number of sets to the update method
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the first set with the union of itself and the second set")
first_set.update(second_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the second set with the union of itself and the first set")
second_set.update(first_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
first_set = {1, 2, 3, 4, 5}
second_set = {True, 5, 6, 7, 8}
third_set = {0, 2, 3, 9, 10}
print("The first set is %r, the second set is %r and the third set is %r" % (first_set, second_set, third_set))
first_set.update(second_set, third_set)
print("Updating the first set with the union of the first, second and third sets, the first set now is %r" % first_set)

