# Documentation
	# pydoc3 str
import string
'''
dir(str)
help(str.method)
help(str)

Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.

'''
# Data
'''
DATA
    boolvalue = True
    floatnumber = 2.3
    integernumber = 12
    string = 'This is a string'
'''
	# Strings are immutable, and ordered.
	# Strings are iterables (we iterate through the characters of the string).
	# Strings are sequences of items (they are ordered by indices).
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.punctuation)
print(repr(string.whitespace))
print(string.digits + string.ascii_letters + string.punctuation + string.whitespace == string.printable)
# String Formatting
print("{0}{1}{0}".format("abra", "cad"))
# String Formating With Named Arguments
print("{x}, {y}".format(y = 12, x = 5))
# str method
string = "This is a string"
integernumber = 12
floatnumber = 2.3
boolvalue = True
print(string, str(string))
print(type(string), type(str(string)))
string = r'This is \na string' # Putting r before the string results in saving the raw string within the variable string that means \n will be printed as it is (we will use this when we get to regular expressions
# Raw Strings escapes escape sequences
print(string, type(string))
x = 12
string = '{} = Twelve'.format(x) # format() is a method of the string object, the period '.' accesses the method of the
# str object and do this variable replacement
print(string, type(string))
string = '%d = Twelve' % (x)
print(string, type(string))
string = str(x) + ' = Twelve'
print(string, type(string))
string = x, '= Twelve'
print(string, type(string))
print(integernumber, str(integernumber))
print(type(integernumber), type(str(integernumber)))
print(floatnumber, str(floatnumber))
print(type(floatnumber), type(str(floatnumber)))
print(boolvalue, str(boolvalue))
print(type(boolvalue), type(str(boolvalue)))
my_list = [1, 2, 3]
my_dict = {1:True, 0:False}
my_tuple = (1, 2, 3)
print(my_list, str(my_list))
print(type(my_list), type(str(my_list)))
print(my_dict, str(my_dict))
print(type(my_dict), type(str(my_dict)))
print(my_tuple, str(my_tuple))
print(type(my_tuple), type(str(my_tuple)))
print(range(1, 101), str(range(1, 101)))
print(type(range(1, 101)), type(str(range(1, 101))))
# Creating an empty string
empty_string = str()
print("This is an empty string: '%s'" % empty_string)
empty_string = ''
print("This is an empty string: '%s'" % empty_string)
# Assigning a string to a variable
string = "a"
print("This is a string: '%s'" % string)
string = "This is a string"
print("This is a string: \"%s\"" % string)
	# Strings can enclosed within a single quotation marks or even a double quotation marks
# String and The Index Operator
my_string = "This is the first line"
print("The string we are working with is: '%s'" % my_string)
print("The character in the first index is: '%s' where, the first index is 0" % my_string[0])
print("The character in the last index is: '%s' where, the last index is len(string)-1" % my_string[len(my_string)-1])
print("We can use negative indices in the index operator to traverse the characters from the end")
print("The character in the last index is: '%s' where, the last index is -1" % my_string[-1])
# String Slicing (Slicing Operator)
my_string = "This is the first line"
	# string[start:[end:step-size]] or string[start:end[:step-size]] or string[:] or string[[start]:end:step-size] or
	# string[[start]:end[:step-size]] where, the default step-size is 1, the default start is 0, and the default end is len(string)
	# Slice the string from the start up to but not including the end with a step-size of step-size
	# We can use negative indices to traverse the characters of the string from the end
print("The whole string is: '%s'" % my_string)
print("The whole string is: '%s'" % my_string[:])
print("The whole string is: '%s'" % my_string[0:])
print("The whole string is: '%s'" % my_string[0:len(my_string)])
print("Some slices of the string are:")
print("The first word of the string is:", my_string[0:4])
print("The first word of the string with a step-size = 2 is:", my_string[0:4:2])
print("The reverse of the string is:", my_string[-1::-1])
print("The second word of the string is:", my_string[5:7])
print("The last word of the string is:", my_string[-4:])
	# We can slice a string and assign the new slice to an entirely new string
my_string_reversed = my_string[-1::-1]
print("The reverse of the string is:", my_string_reversed)
# The len operator
string = "This is a string"
print("The string '%s' has a length of %d" % (string, len(string)))
# Strings with for Loops
	# Traversing the characters of a string (Iterating through the characters of a string)
string = "This is a string"
print("The string is: '%s'" % string)
print("The characters of the string are:")
for c in string:
    print(c)
# The Concatenation Operator (Operator OverLoading)
	# The '+' sign referes to the concatenation operator when it is used with strings
	# In general: str1 + str2 results a new str3 which is nothing but str1 concatenated with str2
string = "This is a string"
my_string = ''
for c in string:
    my_string += c
    print("The result of the concatenation operator is: '%s'" % my_string)
print("The string results from the concatenation operator within the for loop is: '%s'" % my_string)
first_name = "Mohamed"
last_name = "Alansary"
print("The first string is: '%s'" % first_name)
print("The second string is: '%s'" % last_name)
print("Concatenating the two strings, we have:")
full_name = first_name + ' ' + last_name
print("The full name is: '%s'" % full_name)
# The Duplication Operator (Operator OverLoading)
	# The '.' sign referes to the duplication operator when it is used with strings
	# In general: str * int results a new string which is nothing but a duplication of str int times
string = "This is a string "
print("The string is: '%s'" % string)
string_duplicated_twice = string * 2
print("The string '%s' duplicated two times is '%s'" % (string, string_duplicated_twice))
print("Duplicating the string '%s' iteratively five times, we have:" %string)
for i in range(6):
    print(string * i)
# Strings are immutable (We can not change them, but we can assign a slice or a modification to a new string)
string = "This is a test string"
print("The string is: '%s'" % string)
print("We can not assign a value to a part of the string, but we can do the following")
new_string = string[0:5] + 'ls b' + string[-12:]
print("The new string after modification is: '%s'" % new_string)
# Strings and in operator
string = "My name is Mohamed Alansary"
print("The string is \"%s\"" % string)
print("Is 'M' in string? %r" % ('M' in string))
print("Is 'x' in string? %r" % ('x' in string))
print("Is 'ham' in string? %r" % ('ham' in string))
# Strings and Referencing
string1 = "This is a string"
string2 = string1
print("The first string is: '%s'" % string1)
print("The second string is: '%s'" % string2)
string1 = "This"
print("The first string now changed to '%s'" % string1)
print("The second string is not changed at all because string1 now references a new object (Immutability), the second string is: '%s'" % string2)
# Strings and Aliasing
'''
To check whether two variables refer to the same object, you can use the is operator. Python only created one string object, and both a and b refer to it.
'''
a = "This is a string"
b = "This is a string"
print("a is", repr(a))
print("b is", repr(b))
print("Is a and b refere to the same object?")
if a is b:
    print("Yes, it is.")
    print("Changing the value of a does not cause the value of b to change and vice versa")
    a = "This is the new string"
    print("a now is", repr(a))
    print("Testing whether b is changed or not")
    print("b now is", repr(b))
else:
    print("No, it is not.")
# The previous case the two strings were refering to the same string because python keeps small values within the memory
# for later use but when the value gets bigger and bigger it will be reclaimed once its reference counter reaches zero
# and so they will not refere to the same object.
print('-' * 50)
string1 = '*' * 1000000
string2 = '*' * 1000000
print(string1 is string2, id(string1), id(string2), string1 == string2)
string2 = string1 # Aliasing (Aliased Object)
print(string1 is string2, id(string1), id(string2), string1 == string2)
print('-' * 50)
print("Aliasing")
a = "This is a string"
print("a is", repr(a))
b = a
print("We assigned the value of a to b, so b is", repr(b))
print("Is a and b refere to the same object?")
if a is b:
    print("Yes, it is.")
    print("a and b are two references to the same object")
    print("""An object with more than one reference has more than one name, so we say that the object is aliased.""")
    print("Changing the value of a now")
    a = "This is the new string"
    print("a now is", repr(a))
    print("Checking whether b changed or not")
    print("b now is", repr(b))
    print("b doesn't change at all because a now referes to an entirely new object")
else:
    print("No, it is not.")
print("So, Aliasing with Immutable objects doesn't make any difference")
# this \ at the end of the multi-line comment skips the first line (it is not printed on the screen)
multi_line_string = '''\
    Hi there,
\
I'm Mohamed Alansary
I'm a software engineer
'''
# However the following \ is a line continuation
x, y = 1, 2
print(x\
      , y)
print(multi_line_string)
# Data
'''
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
whitespace = '\t\n\x0b\x0c\r '
'''
# Escape Sequences
string = "This is the first line\nThis is the\tsecond\tline\nThis is a back slash \\\nThis is a new line\nThis is a carriage return\r This is a single quote \'\nThis is a double quote \""
print("The raw representation of the string is '%s'" % repr(string))
print("The string is\n'%s'" % string)
print("Carriage Return Simulation")
'''
while True:
    print("/\r-\r\\\r_\r")
'''

test_string = "This is a string"
for index, character in enumerate(test_string):
    print("The character {} is at index {}".format(character, index))
