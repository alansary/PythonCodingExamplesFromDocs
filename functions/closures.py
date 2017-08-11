# Defining a function within a function definition
        # The scope of the function inner is within the function outer, we can not call inner from outside the outer function
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)	# Returns a function call that returns summation of c and d
x, y = 2, 3
res = outer(x, y)	# Is a summation (Value)
print("The summation of %d and %d is %d" % (x, y, res))
print("res is %r and its type is %r" % (res, type(res)))
def outer(a, b):
    def inner():
        return a + b
    return inner	# Returns a function (not a function call)
x, y = 2, 3
res = outer(x, y)	# Is a function (inner function) and the values of a and b are the values that we passed when calling the outer function
print("The summation of %d and %d is %d" % (x, y, res()))	# res() means that we call the function inner, so, we get the returned value a + b
print("res is %r and its type is %r" % (res, type(res)))
def outer(a, b):
    def inner():
        return a + b
    return inner()	# Returns a function call to the inner function that returns a + b
x, y = 2, 3
res = outer(x, y)	# Is a summation (Value)
print("The summation of %d and %d is %d" % (x, y, res))
print("res is %r and its type is %r" % (res, type(res)))

