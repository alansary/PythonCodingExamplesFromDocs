# lstrip()
'''
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
'''
string = "This is a string"
print("Removing the leading whitespaces from the string '%s', we have: '%s'" % (string, string.lstrip()))
string = "    This is a string"
print("Removing the leading whitespaces from the stirng '%s', we have: '%s'" % (string, string.lstrip()))
string = ""
print("Removing the leading whitespaces from the string '%s', we have: '%s'" % (string, string.lstrip()))
string = "    "
print("Removing the leading whitespaces from the string '%s', we have: '%s'" % (string, string.lstrip()))
string = "This is a string"
print("Removing the characters 'Thi' from the beginning of the string '%s', we have: '%s'" % (string, string.lstrip('Thi')))
string = "This is a string"
print("Removing the characters 'Thi' from the beginning of the string '%s', we have: '%s'" % (string, string.lstrip('hiT')))
string = "ThihhisThihhi is a string"
print("Removing the characters 'Thi' from the beginning of the string '%s', we have: '%s'" % (string, string.lstrip('Thi')))
string = "This is a string"
print("Removing the characters 'hi' from the beginning of the string '%s', we have: '%s'" % (string, string.lstrip('hi')))
print("Since T is at the beginning of the string, there is no (hi)s at the beginning and the original string is returned")
string = "\n\t This is a string \n\t"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the leading spaces is '%s'" % repr(string.lstrip()))
string = "@!£$This is a string"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the leading special characters is '%s'" % repr(string.lstrip("£$@!")))

