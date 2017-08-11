# Every thing in python is an object, each object has unique id, type, and a value
x = 12
print(x, type(x), id(x)) # The id is like an address
# Changing the value of x (int is immutable) makes x refere to another object
x = 10
print(x, type(x), id(x))
# We can see that the id changes (Referes to another object)
# Changing its value again to 12, we will find that its id is the same id of 12, this holds only for small values because python
# keeps them within the memory and so their id doesn't change while the execution of the script but for larger values python reclaimes
# them immediately once their reference counter reaches zero and so when they are reserved in memory again they will most likely have
# another id
x = 12
print(x, type(x), id(x))
# printing the id of the value (constant) 12 will give us the same id as x
print(id(12))
print(id(13)) # printing the id of the constant 13
y = 13
print(y, type(y), id(y))
# So in immutable objects we don't change the value of the object but making it refer to an entirely new object
x = 2 ** 1000000
print(id(x), id(2 ** 1000000))
x = 10
x = 2 ** 1000000
print(id(x), id(2 ** 1000000))
