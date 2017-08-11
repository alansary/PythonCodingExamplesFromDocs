def test_fun(val):
    print("The value is %r, its type is %r" % (val, type(val)))
    if val == None: print("None is considered to be False")
    if val: print("True")
    if not val: print("False")
test_fun(None)
test_fun(True)
test_fun(False)
test_fun(1)
test_fun(1.0)
test_fun(0)
test_fun(0.0)
test_fun("")
test_fun([])
test_fun(())
test_fun({})
test_fun(set())
test_fun(-10)
test_fun("string")
test_fun([1, 2, 3])
test_fun({1:True, 0:False})
test_fun((1, 2, 3))
test_fun({1, 2, 3})
test_fun(100)
test_fun(2.5)
