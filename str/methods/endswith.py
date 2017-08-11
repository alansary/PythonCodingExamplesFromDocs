# endswith()
'''
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
'''
string = "This is a string"
print("The string is '%s'" % string)
print("Is the string '%s' ends with the suffix 'g'?" % string)
print(string.endswith('g'))
print("Is the string '%s' ends with the suffix 'ring'?" % string)
print(string.endswith('ring'))
print("Is the string '%s' ends with the suffix 'eng'?" % string)
print(string.endswith('eng'))
print("Is the substring '%s' of the string '%s' ends with the suffix 'a '?" % (string[:10], string))
print(string.endswith('a ', 0, 10))
print("Is the substring '%s; of the string '%s' ends with the suffix 'a'?" % (string[:10], string))
if string.endswith('a', 0, 10):
    print("Yes, it is.")
else:
    print("No, it is not.")
	# Suffix can also be a tuple of string to try.
print("Is the string '%s' ends with 'eng' or 'ang' or 'ing'?" % string)
print(string.endswith(('eng', 'ang', 'ing')))
print("Is the string '%s' ends with 'eng' or 'ang' or 'ong'?" % string)
print(string.endswith(('eng', 'ang', 'ong')))

