# discard()
'''
 |  discard(...)
 |      Remove an element from a set if it is a member.     
 |      If the element is not a member, do nothing.
'''
test_set = {1, 1.5, (1, 2, 3), False, "string"}
print("The test set is %r" % test_set)
print("Discarding 0 from the set, the set now is:")
test_set.discard(0)
print(test_set)
print("Discarding 2.5 from the set, the set now is:")
test_set.discard(2.5)
print(test_set)

