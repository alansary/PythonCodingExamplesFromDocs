# isalpha()
'''
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
'''
	# Alphabetic: abc...zABC...Z
import string
print(string.ascii_letters)
string = "This"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = "This123"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = "This@"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = ""
print("Is all alphanumeric in an empty string '%s'? %s" % (string, string.isalpha()))
string = "123@"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = "1 2 3"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = " "
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))
string = "1.23"
print("Is all alphanumeric in the string '%s'? %s" % (string, string.isalpha()))

