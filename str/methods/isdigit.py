# isdigit()
'''
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
'''
	# Digit: 0...9
import string
print(string.digits)
string = "123"
print("Is the string '%s' is digit? %s" % (string, string.isdigit()))
string = "12.3"
print("Is the string '%s' is digit? %s" % (string, string.isdigit()))
string = "12 3"
print("Is the string '%s' is digit? %s" % (string, string.isdigit()))
string = "12EF"
print("Is the string '%s' is digit? %s" % (string, string.isdigit()))
string = ""
print("Is the string '%s' is digit? %s" % (string, string.isdigit()))

