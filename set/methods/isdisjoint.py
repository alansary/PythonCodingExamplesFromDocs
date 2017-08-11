# isdisjoint()
'''
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
'''
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Is the first set and the second set are disjoint? %r" % first_set.isdisjoint(second_set))
print("The first set and the second set have %r intersection" % first_set.intersection(second_set))
first_set = {1, 1.5, (1, 2, 3), "String"}
second_set = {False, 2.5, (2, 3, 1), "string"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Is the first set and the second set are disjoint? %r" % first_set.isdisjoint(second_set))
print("The first set and the second set have %r intersection" % first_set.intersection(second_set))

