'''
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
'''

fileObject = open('xwrite.txt', 'x')
print(fileObject, "is a file object")
print("Writing 'This is the text' to the file")
n = fileObject.write('This is the text')
print(n, "=", len('This is the text'), "bytes have been written to the file")

