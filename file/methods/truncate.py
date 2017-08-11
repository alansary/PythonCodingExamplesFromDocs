'''
 |  truncate(self, pos=None, /)
 |      Truncate file to size bytes.
 |      
 |      File pointer is left unchanged.  Size defaults to the current IO
 |      position as reported by tell().  Returns the new size.
'''
io = open('truncate.txt', 'r+')
print(io, 'is a file object')
print("The current position is %d" % io.tell())
print("The contents of the file are:")
print(io.read())
print("Seeking to the start of the file, the current position is %d" % io.seek(0, 0))
print("Seeking 50 bytes from the start of the file")
print("The current position is %d" % io.seek(50, 0))
print("Truncating the file to this position")
io.truncate()
print("Seeking to the start of the file, the current position is %d" % io.seek(0, 0))
print("Flushing the IO object to write the changes to the file")
io.flush()
print("The contents of the file now are:")
print(io.read())
print("Truncating the file to 20 bytes")
io.truncate(20)
print("Flushing the IO object to write the changes to the file")
io.flush()
print("Seeking to the start of the file, the current position is %d" % io.seek(0, 0))
print("The contents of the file now are:")
print(io.read())
print("Seeking to the start of the file, the current position is %d" % io.seek(0, 0))
print("Truncating the file to 0 bytes")
io.truncate()
print("Flushing the IO object to write the changes to the file")
io.flush()
print("The current position is %d" % io.tell())
print("The contents of the file now are %s" % io.read())

