"""
 |  detach(self, /)
 |      Separate the underlying buffer from the TextIOBase and return it.
 |      
 |      After the underlying buffer has been detached, the TextIO is in an
 |      unusable state.
"""
fileObject = open('detach.txt', 'rt')
print(fileObject, "is a file object")
detach = fileObject.detach()
print(detach, "is the buffer after disconnecting it from its underlying raw stream (unstable state)")
print(fileObject, "is the detached file object")
try:
    fileObject.read()
except ValueError as e:
    print(e)
