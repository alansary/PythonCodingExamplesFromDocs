# replace()
'''
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
'''
string = "This is a test string"
print("The string '%s' with the sub string '%s' replaced to '%s' is '%s'" % (string, 'is', 'obs', string.replace('is', 'obs')))
print("The string '%s' with the sub string '%s' replaced to '%s' is '%s' (Only the first occurrence)" % (string, 'is', 'obs', string.replace('is', 'obs', 1)))
print("The string '%s' with the sub string '%s' replaced to '%s' is '%s' (Zero occurrences)" % (string, 'is', 'obs', string.replace('is', 'obs', 0)))

