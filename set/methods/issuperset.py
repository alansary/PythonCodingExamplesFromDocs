# issuperset()
'''
 |  issuperset(...)
 |      Report whether this set contains another set.
'''
first_set = {1, 1.5, (1, 2, 3), False, "string"}
second_set = {1, 1.5, (2, 3, 1), True, "String", 3, "x"}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Is the first set is a superset of the second set? %r" % first_set.issuperset(second_set))
print("Is the second set is a superset of the first set? %r" % second_set.issuperset(first_set))
first_set = {1, 2, 3}
second_set = {1, 3}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Is the first set is a superset of the second set? %r" % first_set.issuperset(second_set))
print("Is the second set is a superset of the first set? %r" % second_set.issuperset(first_set))
first_set = {1, 3}
second_set = {1, 3}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("Is the first set is a superset of the second set? %r" % first_set.issuperset(second_set))
print("Is the second set is a superset of the first set? %r" % second_set.issuperset(first_set))

