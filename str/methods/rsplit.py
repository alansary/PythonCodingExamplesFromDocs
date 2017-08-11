# rsplit()
'''
|  rsplit(...)
|      S.rsplit(sep=None, maxsplit=-1) -> list of strings
|      
|      Return a list of the words in S, using sep as the
|      delimiter string, starting at the end of the string and
|      working to the front.  If maxsplit is given, at most maxsplit
|      splits are done. If sep is not specified, any whitespace string
|      is a separator.
'''
string = ""
print("Right spliting an empty string '%s' on spaces, we have: '%r'" % (string, string.rsplit()))
string = "This is a string"
print("Right spliting the string '%s' on spaces, we have: '%r'" % (string, string.rsplit()))
string = "The,separator,is,a,comma"
print("Right spliting the string '%s' on commas, we have: '%r'" % (string, string.rsplit(',')))
string = "The, separator, is, comma, followed, by, a, space"
print("Right spliting the string '%s' on comma follwed by a space, we have: '%r'" % (string, string.rsplit(', ')))
string = "This is the first line"
print("Right spliting the string '%s' spaces, and max-split is 2, we have: '%r'" % (string, string.rsplit(' ', 2)))
print("If the separator doesn't exist, we get: '%r'" % string.rsplit('xox'))

