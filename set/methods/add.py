# add()
'''
 |  add(...)
 |      Add an element to a set.     
 |      This has no effect if the element is already present.
'''
test_set = {1, 1.5, (1, 2, 3), False, "string"}
print("Our test set is %r" % test_set)
print("Adding 2 to the set, we have:")
test_set.add(2)
print(test_set)
print("Adding 2 again to the set will have no effect on the set because the element already exists")
test_set.add(2)
print("The test set is %r after adding the 2 again" % test_set)

