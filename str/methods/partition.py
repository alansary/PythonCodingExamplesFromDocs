# partition()
'''
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
'''
string = "This is a string"
print("Partitioning the string '%s' on ' is ' as a separator, we have: '%s'" % (string, string.partition(' is ')))
print("The type of the result is '%s'" % type(string.partition(' is ')))
string = "This is a string"
print("Partitioning the string '%s' on ' is x' as a separator, we have: '%s'" % (string, string.partition(' is x')))
string = "This is a test string"
head, sep, tail = string.partition("is")
print("head:", head, "sep:", sep, "tail:", tail)
print(string.partition("is"))
head, sep, tail = string.partition("haha")
print("head:", head, "sep:", sep, "tail:", tail)
print(string.partition("haha"))

