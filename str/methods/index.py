# index()
'''
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
'''
string = "This is a string"
print("The string is '%s'" % string)
print("""index() is just like find(), but the main difference is that find() returns -1 when the substring is not found\
 and index() raise a ValueError when the substring is not found""")
print("We can handle found() using an if condition and handle index() using try and except")
print("Finding the index of the substring 'This' in the string -> Result =", string.index('This'), end = '')
print(", it should be 0")
print("Finding the index of the substring 'is' in the string -> Result =", string.index('is'), end = '')
print(", it should be 2")
print("Finding the index of the substring 'is' in the string, starting with index 3 -> Result =", string.index('is', 3), 
	end = '')
print(", it should be 5")
print("""Finding the index of the substring 'is' in the string, starting with index 3 and ending with 5
 (It will raise a ValueError if we don't handle it using try and except""")
try:
    string.index('is', 3, 6)
    print("The index is %d" % string.index('is', 3, 6))
except:
    print("The substring 'is' is not found in the string starting with index 3 and ending with 5")
print("Finding the index of the substring 'isasa' in the string -> Result = Raise a ValueError",
	string.index('isasa'), end = '')

