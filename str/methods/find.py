# find()
'''
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
'''
string = "This is a string"
print("The string is '%s'" % string)
print("The lowest substring 'is' is found at index %d in the string '%s'" % (string.find('is'), string))
print("The lowest substirng 'is' from the third index is found at index %d in the string '%s'" % (string.find('is', 3), string))
print("The lowest substring 'iss' is not found in the string '%s', it will return -1 failure" % string)
if string.find('iss') == -1:
    print("There is a failure finding the index of a substring that is not found in the string")
else:
    print("The starting index of the lowest substirng 'iss' in the string is %d" % string.find('iss'))
print("Finding the index of the substring 'This' in the string -> Result =", string.find('This'), end = '')
print(", it should be 0")
print("Finding the index of the substring 'is' in the string -> Result =", string.find('is'), end = '')
print(", it should be 2")
print("Finding the index of the substring 'is' in the string, starting with index 3 -> Result =", 
	string.find('is', 3), end = '')
print(", it should be 5")
print("Finding the index of the substring 'is' in the string, starting with index 3 and ending with 5 -> Result =", 
	string.find('is', 3, 6), end = '')
print(", it should be -1")
print("Finding the index of the substring 'isasa' in the string -> Result =", string.find('isasa'), end = '')
print(", it should be -1")

