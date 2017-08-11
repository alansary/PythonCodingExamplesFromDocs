# Comprehension means doing the same thing with more than one method (Do it the pythonic way)
test_list = []
print("The list is %r" % test_list)
for e in range(1, 10, 2):
    test_list.append(e)
print("The list now is %r" % test_list)
test_list = []
print("The list is %r" % test_list)
test_list = list(range(1, 10, 2))
print("The list now is %r" % test_list)
test_list = []
print("The list is %r" % test_list)
test_list = [e for e in range(1, 10, 2)]
print("The list now is %r" % test_list)
test_list = []
print("The list is %r" % test_list)
test_list = [e for e in range(1, 10, 1) if e % 2 == 1]
print("The list now is %r" % test_list)
test_list = []
print("The list is %r" % test_list)
for e in range(1, 10, 1):
    if e % 2 == 1:
        test_list.append(e)
print("The list now is %r" % test_list)
test_list = []
print("The list is %r" % test_list)
rows = range(1, 4, 1)
cols = range(1, 3, 1)
for row in rows:
    for col in cols:
        test_list.append((row, col))
print("The list now is %r, the elements of the list are:" % test_list)
for e in test_list:
    print(e, end = ' ')
print("")
test_list = []
print("The list is %r"  % test_list)
test_list = [(row, col) for row in range(1, 4) for col in range(1, 3)]
print("The list now is %r, the elements of the list are:" % test_list)
for e in test_list:
    print(e, end = ' ')
print("")
test_list = []
print("The list is %r" % test_list)
test_list = [[e1, e2] for e1 in range(0, 11, 1) if e1 % 2 == 0 for e2 in range(0, 10, 1) if e2 % 2 == 1]
print("The list now is %r" % test_list)

