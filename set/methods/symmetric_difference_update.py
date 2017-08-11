# symmetric_difference_update()
'''
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
'''
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the first set with the symmetric difference of itself and the second set")
first_set.symmetric_difference_update(second_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Updating the second set with the symmetric difference of itself and the first set")
second_set.symmetric_difference_update(first_set)
print("The first set now is %r and the second set is %r" % (first_set, second_set))

