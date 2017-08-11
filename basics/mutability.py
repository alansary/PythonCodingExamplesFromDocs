# Every thing in python is an object, each object has unique id, type, and a value
x = 12
print(x, type(x), id(x)) # The id is like an address
# Changing the value of x (int is immutable) makes x refere to another object
x = 10
print(x, type(x), id(x))
# We can see that the id changes (Referes to another object)
# Changing its value again to 12, we will find that its id is the same id of 12, this doesn't hold for large values since python
# reclames all large values once its reference counter reaches zero, but it keeps the small values within the memory that's why
# when we assigned x to 12 again it have the same id
x = 12
print(x, type(x), id(x))
# printing the id of the value (constant) 12 will give us the same id as x
print(id(12))
x = 2 ** 1000000
print(id(x))
print(id(2 ** 1000000))
x = 10
x = 2 ** 1000000
print(id(x))
print(id(2 ** 1000000))
print(id(13)) # printing the id of the constant 13
y = 13
print(y, type(y), id(y))
# So in immutable objects we don't change the value of the object but making it refer to an entirely new object
z = 12
x = 12
print(z, type(z), id(z))
print(x == z, x is z) # The is operator compares the id rather than comparing the value
# numbers, strings, booleans and tuples are immutable while dictionaries, lists, and sets are mutable
d1 = dict(x = 32)
d2 = dict(x = 32)
print(d1, type(d1), id(d1))
print(d2, type(d2), id(d2))
print(d1 == d2, d1 is d2)
x = True
y = True
print(x, type(x), id(x))
print(y, type(y), id(y))
print(True, type(True), id(True))
# None, True and False are singelton objects and so identity is a good way to test for them
x = None
if x is None: print("x is None")
