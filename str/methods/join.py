# join()
'''
 |  join(...)
 |      S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
'''
	# Note: iterable of strings
print("Joining the characters of the word 'This' by spaces, we have:")
print(' '.join("This"))
print("The type of the returned result: %s" % type(' '.join("This")))
print("Joining the characters of the word 'This' by empty string, we have:")
print(''.join("This"))
print("The type of the returned result: %s" % type(''.join("This")))
print("Joining the elements of the list '['This', 'That']' by the word '@@11@@', we have:")
print('@@11@@'.join(['This', 'That']))
print("The type of the returned result: %s" % type('@@11@@'.join(['This', 'That'])))
print("Joining the elements of the tuple '('1', '2', '3')' by the word 'Hello', we have:")
print('Hello'.join(('1', '2', '3')))
print("The type of the returned result: %s" % type('Hello'.join(('1', '2', '3'))))
print("Joining the numbers (as strings) from 0 to 9 by spaces, we have:")
l = list()
for i in range(0, 10):
    l.append(str(i))
print(' '.join(l))
print("The type of the returned result: %s" % type(' '.join(l)))
	# Other Examples:
string = "--Separator--"
iterlist = ["One", '2', "False", "True", "2.34"]
itertuple = ("One", "2", "False", "True", "2.34")
iterDict = {"One":1, '2':2, "False":True, "True":False, "2.34":3}
print(string, '\n', iterlist, '\n', itertuple, '\n', iterDict)
print(string.join(iterlist))
print(string.join(itertuple))
print(string.join(iterDict))

