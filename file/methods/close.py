"""
     |  close(...)
     |      close() -> None.  Close the file.
     |      A closed file cannot be used for further I/O operations.  close() may be
     |      called more than once without error.
"""
fileObject = open('close.txt', 'a+t')
print(fileObject, "is a file obejct")
n = fileObject.write("This is the fourth line")
print(n, '=', len('This is the fourth line'), "have been written to the file")
fileObject.close()
print("The IO object", fileObject, "has been flushed and closed")

