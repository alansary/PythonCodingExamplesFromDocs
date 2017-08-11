'''
     |  flush(...)
     |      Flush write buffers, if applicable.
     |      This is not implemented for read-only and non-blocking streams.
'''
# If we work with big data, we maybe need to flush the file at some point after some modifications and not waiting to close it to write the modifications
# Run the following script in python IDLE to keep track of what happens
fileObject = open('flush.txt', 'a+t')
print(fileObject, "is a file object")
text = '# '
for x in range(1, 101, 1):
    fileObject.write(text * x + '\n') # At this point, the file is modified, but not saved yet
    fileObject.flush() # The file is updated, and any modifications are saved
fileObject.close() # The file is saved and the connection is closed

