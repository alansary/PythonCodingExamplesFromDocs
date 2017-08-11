'''
 |  seek(self, cookie, whence=0, /)
 |      Change stream position.
 |      
 |      Change the stream position to the given byte offset. The offset is
 |      interpreted relative to the position indicated by whence.  Values
 |      for whence are:
 |      
 |      * 0 -- start of stream (the default); offset should be zero or positive
 |      * 1 -- current stream position; offset may be negative
 |      * 2 -- end of stream; offset is usually negative
 |      
 |      Return the new absolute position.
'''

fileObject = open('seek.txt', 'a+b')
print(fileObject, "is a file object")
print("My current position is %d" % fileObject.tell())
print("Seeking to the start of the file")
fileObject.seek(0, 0)
print("My current position is %d" % fileObject.tell())
print("The first two characters in the file:")
print(fileObject.read(2))
print("My current position is %d" % fileObject.tell())
print("Seeking two bytes from the current position")
curr_pos = fileObject.seek(2, 1)
print("My current position is %d" % curr_pos)
print("Seeking to the end of file")
print("My current position is %d" % fileObject.seek(0, 2))
print("Seeking ten bytes from the EOF")
print("My current position is %d" % fileObject.seek(10, 2))
print("Writing b'Appended' from this position")
print("%d bytes have been written to the file" % fileObject.write(b'Appended'))
print("My current position is %d" % fileObject.tell())
print("Writing b'Appended' from this position")
print("%d bytes have been written to the file" % fileObject.write(b'Appended'))
print("My current position is %d" % fileObject.tell())
print("The current position again is %d" % fileObject.tell())
print("Seeking one byte from this position")
print("My current position is %d" % fileObject.seek(fileObject.tell()+1, 0))
    # Odd behavior
    # When using seek(x, 1) it seeks backware 10 bytes at first then
    # seeks x forward
    # However, when we seek fileObject.tell() + 1 from the beginning, it
    # works just fine
print("Writing b'Appended' from this position")
print("%d bytes have been written to the file" % fileObject.write(b'Appended'))
print("My current position is %d" % fileObject.tell())
print("Seeking to the start of the file")
print("My current position is %d" % fileObject.seek(0))
print("Flushing the IO object to save changes to the file")
fileObject.flush()
print("The contents of the file are:")
fileObject = open('seek.txt', 'r+t')
print(fileObject.read())

fileObject = open('seek.txt', 'r')
x = 0
for c in fileObject.read():
    x += 1
print(x, "is the final number of bytes in the file execluding the bytes we exceeded beyond the EOF")

# Note that any seek beyond the EOF will not be counted.
