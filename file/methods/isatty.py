'''
 |  isatty(self, /)
 |      Return whether this is an 'interactive' stream.
 |      
 |      Return False if it can't be determined.
'''
fileObject = open('isatty.txt', 'a')
print(fileObject, 'is a file object')
print("%r.isatty() ? %r" % (fileObject, fileObject.isatty()))

