'''
 |  read(self, size=-1, /)
 |      Read at most n characters from stream.
 |      
 |      Read from underlying buffer until we have n characters or we hit EOF.
 |      If n is negative or omitted, read until EOF.
'''
fileObject = open('read1.txt', 'r')
print(fileObject, "is a file object")
print("The contents of the file are:")
print(fileObject.read())
fileObject.detach()
fileObject = open('read2.txt', 'r')
print(fileObject, "is a file object")
print("Reading 12 bytes of the file, we have:")
print(fileObject.read(12))
print("Reading another 8 bytes of the file, we have:")
print(fileObject.read(8))
print("Reading to the EOF, we have:")
print(fileObject.read(None))
fileObject.detach()
fileObject = open('read3.txt', 'r')
print(fileObject, "is a file object")
print("Reading to the EOF, we have:")
print(fileObject.read(-5))
print("On EOF read returns empty string:")
print(fileObject.read())

