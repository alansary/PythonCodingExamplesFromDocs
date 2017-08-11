# isalnum()
'''
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
'''
	# Alphanumeric Characters: abc...zABC...Z012...9
import string
print(string.ascii_letters + string.digits)
string = "This"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = "This123"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = "This@"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = ""
print("Is all alphanumeric in an empty string '%s'? %s" % (string, string.isalnum()))
string = "123@"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = "1 2 3"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = " "
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))
string = "1.23"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalnum()))

