# strip()
'''
 |  strip(...)
 |      S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
'''
string = "This is a string"
print("Removing the trailing and the leading whitespaces from the string '%s', we have: '%s'" % (string, string.strip()))
string = "        This is a string    "
print("Removing the trailing and the leading whitespaces from the stirng '%s', we have: '%s'" % (string, string.strip()))
string = ""
print("Removing the trailing and the leading whitespaces from the string '%s', we have: '%s'" % (string, string.strip()))
string = "    "
print("Removing the trailing and the leading whitespaces from the string '%s', we have: '%s'" % (string, string.strip()))
string = "This is a string"
print("Removing the characters 'thinG' from the end and the beginning of the string '%s', we have: '%s'" % (string, string.strip('thinG')))
string = "This is a string"
print("Removing the characters 'hTgni' from the end and the beginning of the string '%s', we have: '%s'" % (string, string.strip('hTgni')))
string = "ThihhisThihhi is a strinlgiinggg"
print("Removing the characters 'Thing' from the end and the beginning of the string '%s', we have: '%s'" % (string, string.strip('Thing')))
string = "This is a string"
print("Removing the characters 'hin' from the end and the beginning of the string '%s', we have: '%s'" % (string, string.strip('hin')))
print("Since g is at the end of the string, there is no (hin)s at the end and the original string is returned,")
print("also T is at the beginning of the string, there is no (hin)s at the beginning and the original string is returned.")
string = "\n\t This is a string \n\t"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the trailing and leading spaces is '%s'" % repr(string.strip()))
string = "@!£$This is a string@!£$"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the trailing and leading special characters is '%s'" % repr(string.strip("£$@!")))

