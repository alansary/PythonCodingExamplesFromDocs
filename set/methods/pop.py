# pop()
'''
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
'''
	# Note that: pop function with sets is the same as popitem function with dicts
test_set = {1, 1.5, (1, 2, 3), False, "string"}
print("Our test set is %r" % test_set)
print("Popping an element of the set, we have:")
popped = test_set.pop()
print("The list is %r and the popped element is %r" % (test_set, popped))
print("Popping an element of the set, we have:")
popped = test_set.pop()
print("The list is %r and the popped element is %r" % (test_set, popped))
print("Popping an element of the set, we have:")
popped = test_set.pop()
print("The list is %r and the popped element is %r" % (test_set, popped))
print("Popping an element of the set, we have:")
popped = test_set.pop()
print("The list is %r and the popped element is %r" % (test_set, popped))
if (len(test_set)) > 0:
    print("Popping an element of the set, we have:")
    popped = test_set.pop()
    print("The list is %r and the popped element is %r" % (test_set, popped))
else:
    print("We can not pop from an empty set, trying to pop from an empty set will raise a KeyError")
print("Popping an element of the set while the set is empty (raise KeyError)")
popped = test_set.pop()

