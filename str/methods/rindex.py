# rindex()
'''
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
'''
string = "This is a string"
print("Finding the index of the sub string '%s' in the string '%s'\nThe index is %d" % ('is', string, string.rindex('is')))
print("Finding the index of the sub string '%s' in the string '%s', searching in the slice '%s'" % ('i', string, string[2:6]))
print("The highest index is %d" % string.rindex('i', 2, 6))
print("The index of the sub string '%s' is not found in the string '%s' (Raise A Value Error)" % ('iss', string))
print(string.rindex('iss'))

