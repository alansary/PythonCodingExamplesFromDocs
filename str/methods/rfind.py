# rfind.py
'''
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
'''
string = "This is a string"
print("Finding the highest index of the sub string '%s' in the string '%s'\nThe highest index is %d" % ('is', string, string.rfind('is')))
print("Finding the highest index of the sub string '%s' in the string '%s', searching the slice '%s'" % ('i', string, string[2:6]))
print("The highest index is %d" % string.rfind('i', 2, 6))
print("The highest index of the sub string '%s' in the string '%s' is not found, return -1 (%d)" % ('strong', string, string.find('strong')))

