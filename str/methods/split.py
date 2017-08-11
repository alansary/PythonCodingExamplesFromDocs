# split()
'''
|  split(...)
|      S.split(sep=None, maxsplit=-1) -> list of strings
|      
|      Return a list of the words in S, using sep as the
|      delimiter string.  If maxsplit is given, at most maxsplit
|      splits are done. If sep is not specified or is None, any
|      whitespace string is a separator and empty strings are
|      removed from the result.
'''
string = ""
print("Spliting an empty string '%s' on spaces, we have: '%r'" % (string, string.split()))
string = "This is a string"
print("Spliting the string '%s' on spaces, we have: '%r'" % (string, string.split()))
string = "The,separator,is,a,comma"
print("Spliting the string '%s' on commas, we have: '%r'" % (string, string.split(',')))
string = "The, separator, is, comma, followed, by, a, space"
print("Spliting the string '%s' on comma follwed by a space, we have: '%r'" % (string, string.split(', ')))
string = "This is the first line"
print("Spliting the string '%s' spaces, and max-split is 2, we have: '%r'" % (string, string.split(' ', 2)))
print("If the separator doesn't exist, we get: '%r'" % string.split('xox'))

