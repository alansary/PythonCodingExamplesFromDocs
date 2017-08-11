# copy()
'''
 |  copy(...)
 |      Return a shallow copy of a set.
'''
set1 = {1, 1.5, (1, 2, 3), False, "string"}
print("Our first set is %r" % set1)
set2 = set1.copy()
print("Our second set, %r is a shallow copy of the first set" % set2)
print("Is the first set == the second set? %r" % (set1 == set2))
print("Is the first set is the second set? %r" % (set1 is set2))
set3 = {1, 1.5, (1, 2, 3), False, "string"}
print("The third set is %r, it is assigned the same value as the first set" % set3)
print("Is the first set == the third set? %r" % (set1 == set3))
print("Is the first set is the third set? %r" % (set1 is set3))
set4 = set(set1)
print("The fourth set is %r, it is initialized from the first set" % set4)
print("Is the first set == the fourth set? %r" % (set1 == set4))
print("Is the first set is the fourth set? %r" % (set1 is set4))
set5 = set1
print("The fifth set is %r, it is assigned to the first set" % set5)
print("Is the first set == the fifth set? %r" % (set1 == set5))
print("Is the first set is the fifth set? %r" % (set1 is set5))

