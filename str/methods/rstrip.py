# rstrip()
'''
|  rstrip(...)
|      S.rstrip([chars]) -> str
|      
|      Return a copy of the string S with trailing whitespace removed.
|      If chars is given and not None, remove characters in chars instead.
'''
string = "This is a string"
print("Removing the trailing whitespaces from the string '%s', we have: '%s'" % (string, string.rstrip()))
string = "This is a string    "
print("Removing the trailing whitespaces from the stirng '%s', we have: '%s'" % (string, string.rstrip()))
string = ""
print("Removing the trailing whitespaces from the string '%s', we have: '%s'" % (string, string.rstrip()))
string = "    "
print("Removing the trailing whitespaces from the string '%s', we have: '%s'" % (string, string.rstrip()))
string = "This is a string"
print("Removing the characters 'inG' from the end of the string '%s', we have: '%s'" % (string, string.rstrip('inG')))
string = "This is a string"
print("Removing the characters 'gni' from the end of the string '%s', we have: '%s'" % (string, string.rstrip('gni')))
string = "ThihhisThihhi is a strinlgiinggg"
print("Removing the characters 'ing' from the end of the string '%s', we have: '%s'" % (string, string.rstrip('ing')))
string = "This is a string"
print("Removing the characters 'in' from the end of the string '%s', we have: '%s'" % (string, string.rstrip('in')))
print("Since g is at the end of the string, there is no (in)s at the end and the original string is returned")
string = "\n\t This is a string \n\t"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the trailing spaces is '%s'" % repr(string.rstrip()))
string = "@!£$This is a string@!£$"
print("The raw representation of the string is '%s'" % repr(string))
print("The raw representation of the string after removing the trailing special characters is '%s'" % repr(string.rstrip("£$@!")))

