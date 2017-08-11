# isnumeric()
'''
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
'''
	# Numeric: 0, 1, 3, ..., 9
import string
print(string.digits)
string = "This is a string"
print("Is all numeric in the string '%s'? %s" % (string, string.isnumeric()))
string = "123.3"
print("Is all numeric in the string '%s'? %s" % (string, string.isnumeric()))
string = "123"
print("Is all numeric in the string '%s'? %s" % (string, string.isnumeric()))
string = ""
print("Is all numeric in the string '%s'? %s" % (string, string.isnumeric()))
string = "224@"
print("Is all numeric in the string '%s'? %s" % (string, string.isnumeric()))

