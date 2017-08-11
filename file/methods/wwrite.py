'''
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
'''

fileObject = open('wwrite.txt', 'w')
print(fileObject, "is a file object")
print("Writing 'This is the text' to the file")
text = 'This is the text'
n = fileObject.write(text)
print(n, "bytes have been written to the file")

