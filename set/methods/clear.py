# clear()
'''
 |  clear(...)
 |      Remove all elements from this set.
'''
test_set = {1, 1.5, (1, 2, 3), False, "string"}
print("Our test set is %r" % test_set)
print("Clearing the test set %r, we have:" % test_set)
test_set.clear()
print(test_set)

