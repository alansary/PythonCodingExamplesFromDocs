# isprintable()
'''
 |  isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
'''
	# Any character we can print on the screen is a printable character, including spaces
	# printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
import string
print(repr(string.printable))
print(repr(string.digits + string.ascii_letters + string.punctuation + string.whitespace))
string = "This is a string"
print("'%s' is print table? %s" % (string, string.isprintable()))
string = "This is @"
print("'%s' is print table? %s" % (string, string.isprintable()))
string = "CAPITAL small @_123.#~'£$%\\/"
print("'%s' is print table? %s" % (string, string.isprintable()))
string = "\t"
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = ""
print("'%s' is print table? %s" % (string, string.isprintable()))
string = "\n"
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = "      "
print("'%s' is print table? %s" % (string, string.isprintable()))
string = '\r'
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = '\v'
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = '\x0b'
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = '\x0c'
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))
string = " "
print("The raw representation of the string is '%s'" % repr(string))
print("'%s' is print table? %s" % (string, string.isprintable()))

