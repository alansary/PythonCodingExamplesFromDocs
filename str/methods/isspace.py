# isspace()
'''
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
'''
	# is space: ' ' Space, '\t' Horizontal Tab, '\n' New Line, '\r' Carriage Return, '\x0b' Vertical Tab, '\x0c' Vertical Tab, '\v' Vertical Tab
import string
print(repr(string.whitespace))
string = "     "
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\t"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = '\n'
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = '\x0b'
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\x0c"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "a"
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "1"
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "@"
print("The string '%s' is space? %s" % (string, string.isspace()))
string = ''
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\r"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\'"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\\"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))
string = "\v"
print("The raw representation of the string is '%s'" % repr(string))
print("The string '%s' is space? %s" % (string, string.isspace()))

