test_set = set()
print("The set is %r" % test_set)
test_set = {element for element in range(0, 11, 1) if element % 2 == 0}
print("The set now is %r" % test_set)
test_set = set()
print("The set now is %r" % test_set)
test_set = {(e1, e2) for e1 in range(0, 11, 1) if e1 % 2 == 0 for e2 in range(0, 10, 1) if e2 % 2 == 1}
print("The set now is %r" % test_set)

