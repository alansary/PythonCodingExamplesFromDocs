'''
 |  fileno(self, /)
 |      Returns underlying file descriptor if one exists.
 |      
 |      OSError is raised if the IO object does not use a file descriptor.
'''
fileObject = open('fileno.txt', 'at')
print(fileObject, "is a file object")
try:
    fileno = fileObject.fileno()
    print(fileno, "is the underlying file descriptor")
except OSError as e:
    print(e)
