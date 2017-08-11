# startswith()
'''
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
'''
string = "This is a string"
print("Is the string '%s' starts with 'thi'? '%r'" % (string, string.startswith('thi')))
print("Is the string '%s' starts with 'Thi'? '%r'" % (string, string.startswith('Thi')))
print("Is the sub-string '%s' of the string '%s' starts with 's a'? '%r'" % (string[6:], string, string.startswith('s a', 6)))
print("Is the sub-string '%s' of the string '%s' starts with 's a'? '%r'" % (string[6:9], string, string.startswith('s a', 6, 9)))
print("Is the string '%s' starts with 'h'? '%r'" % (string, string.startswith('h')))
string = ""
print("Is the empty string '%s' starts with ' '? '%r'" % (string, string.startswith(' ')))
print("Is the empty string '%s' starts with ''? '%r'" % (string, string.startswith('')))
string = "This is a string"
print("Is the sub-string '%s' of the string '%s' starts with 'a s'? '%r'" % (string[-8:-5], string, string.startswith('a s', -8, -5)))

