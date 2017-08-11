def test_fun(x, y):
    print("Call with %d and %d" % (x, y))
    if x == y: print("%d equals %d" % (x, y))
    if x != y: print("%d doesn't equal to %d" % (x, y))
    if x >= y: print("%d is greater than or equal to %d" % (x, y))
    if x > y: print("%d is greater than %d" % (x, y))
    if x <= y: print("%d is less than or equal to %d" % (x, y))
    if x < y: print("%d is less than %d" % (x, y))
test_fun(10, 10)
test_fun(8, 10)
test_fun(10, 8)

