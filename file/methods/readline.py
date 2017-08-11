'''
 |  readline(self, size=-1, /)
 |      Read until newline or EOF.
 |      
 |      Returns an empty string if EOF is hit immediately.
'''
fileObject = open('readline.txt', 'r')
print(fileObject, "is a file object")
print("The first line is:")
print(fileObject.readline())
print("Reading 25 bytes of the second line which is of length 24:")
print(fileObject.readline(25))
print("Reading 12 bytes of the third line:")
print(fileObject.readline(12))
print("Reading till the end of the third line:")
print(fileObject.readline())
print("Now we are at the EOF, trying to read a line")
print(fileObject.readline())

