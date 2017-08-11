import math
# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# assert False does nothing and assert True raise AssertionError
# The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.
# Note that: The type of int, float, str, tuple, list, set, dict, ... are of <class 'type'>
def duplication(x, y):
    assert type(x) == type("this is a string"), "The first argument must be a string, you input: " + str(x) + " which is of type " + str(type(x))
    assert type(y) == type(100), "The second argument must be an integer, you input: " + str(y) + " which is of type " + str(type(y))
    assert y >= 0, "The second argument must be greater than or equal to 0, you input: " + str(y) + " which is less than 0"
    return x * y
#print(duplication(2, 3))		# AssertionError
#print(duplication("string", "s"))	# AssertionError
#print(duplication(2, "string"))	# AssertionError
#print(duplication("string", -1))	# AssertionError
print(duplication("string", 0))
print(duplication("string", 10))
def take_log(x, y):
    assert x > 0, "x must be greater than 0, you input:" + str(x)
    assert y > 0, "y must be greater than 0, you input:" + str(y)
    print(math.log(x/y))
#take_log(0, 1)		# AsseritonError
#take_log(-1, 1)	# AssertionError
take_log(1, 1)
#take_log(1, 0)		# AssertionError
#take_log(1, -1)	# AssertionError

