# remove()
'''
 |  remove(...)
 |      Remove an element from a set; it must be a member.   
 |      If the element is not a member, raise a KeyError.
'''
test_set = {1, 1.5, (1, 2, 3), False, "string"}
print("Our test set is %r" % test_set)
if False in test_set:
    print("Removing False from the set, we have:")
    test_set.remove(False)
    print(test_set)
else:
    print("False is not a member of the set try to remove it and you will get a KeyError")
if 2 in test_set:
    print("Removing 2 from the set, we have:")
    test_set.remove(2)
    print(test_set)
else:
    print("2 is not a member of the set try to remove it and you will get a KeyError")
print("Removing an element that is not a member of the set will raise a KeyError if we don't handle it")
print("Trying to remove 2.5 of the set %r" % test_set)
test_set.remove(2.5)

