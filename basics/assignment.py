# The left side is a comma separated list of variables; the right side is a comma separated list of
# expressions/values/variables/Data Structures.
# The number of variables on the left and the number of expressions/values/variables/Data Structures on the right have to be the same.
# A value in parentheses is not a tuple:
# Note that 1 == True, 0 == False (They are the same values)
t = ('a')
print("The type of %s is" %(t), type(t))
x, y, z = 1, 2, 3 # This is not a tuple
(a, b, c) = (4, 5, 6) # This is not a tuple
print("The value of x is %d\ty is %d\tz is %d," % (x, y, z), "they are of types", type(x), type(y), type(z))
print("Changing the value of x to 2, y to 4, we have")
x, y = 2, 4
print((x, y, z))
print('{}, {}, {}'.format(x, y, z))
print("Swapping the value of y and z, we have")
y, z = z, y
print((x, y, z))
print("The value of a is %d\tb is %d\tc is %d," % (a, b, c), "they are of types", type(a), type(b), type(c))
x, y, z = [1, 2, 3], ("One", "Two", "Three"), {1:"One", 2:"Two", 3:"Three"}
print("The value of x is %r\ty is %r\tz is %r," % (x, y, z), "they are of types", type(x), type(y), type(z))
addr = 'monty@python.org'
print("The address is \"%s\"" % addr)
uname, domain = addr.split('@')
print("Spliting the address on \'@\', the list is %r" % addr.split('@'))
print("The user name is %s and the domain is %s" % (uname, domain))
my_list = [1, 2, 3]
print("The list is %r" % my_list)
x, y, z = my_list
print("The first element of the list is %d" % x)
print("The second element of the list is %d" % y)
print("The third element of the list is %d" % z)
my_dict = {"This is one":1, 5:"This is five", False:"This is false"}
print("The dictionary is %r" % my_dict)
x, y, z = my_dict
print("The first printed key of the dictionary is %r" % x)
print("The second printed key of the dictionary is %r" %y)
print("The third prined key of the dictionary is %r" %z)
my_tuple = ("This is the first element", False, 3)
print("The tuple is %r" % (my_tuple,))
x, y, z = my_tuple
print("The first element of the tuple is %s" % x)
print("The second element of the tuple is %r" % y)
print("The third element of the tuple is %d" % z)
def edit_fun():
    return 2, 3
print("Getting the returned value of the function within two variables x and y")
x, y = edit_fun()
print("The value of x is %d and the value of y is %d" % (x, y))
email_address = "mohamed_alansary@gmail.com"
print("My e-mail address is %s" % email_address)
print("Partitioning this e-mail on '@' as a separator, we have: %r" % (email_address.partition('@')))
partitions = email_address.partition('@')
head, sep, tail = partitions
print("The head is %s, the separator is %s, and the tail is %s" % (head, sep, tail))
