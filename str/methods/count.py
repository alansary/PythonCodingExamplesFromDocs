# count()
'''
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
'''
	# Note: Counts from the start index up to but not including the end index
	# The default of the start index is 0
	# The default of the end index is len(string)
string = "aaa"
print("The string is: '%s' and the number of occurrences of 'a' within the string is %d" % (string, string.count('a')))
string = "This is a string"
print("The number of occurrences of the substring 'is' in the string '%s' is %d" % (string, string.count('is')))
print("The number of occurrences of the substring 'is' in the string '%s' from index 0 to the fifth index is %d"
	% (string, string.count('is', 0, 6)))
print("The number of occurrences of the substring 'is' in the string '%s' from index 0 to the sixth index is %d"
	% (string, string.count('is', 0, 7)))
print("The number of occurrences of the substring 'str' in the string '%s' from index 10 to the end is %d"
	% (string, string.count('str', 10)))

