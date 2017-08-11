'''
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
'''

fileObject = open('awrite.txt', 'a')
print(fileObject, "is a file object")
print("Appending", repr('This is the fourth line'), "to the file")
text = 'This is the fourth line'
n = fileObject.write(text)
print(n, "bytes have been appended to the file")

