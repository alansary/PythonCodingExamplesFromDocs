# pydoc3 open/io/codecs

'''
# Read mode 'r' opens a file for read (FileNotFoundError is raised when the file doesn't exist)
# Write mode 'w' opens a file for write (truncates the file before writing) and create it if it doesn't exist
# Appending mode 'a' opens the file for appending (writing) and create it if it doesn't exist
# X mode 'x' creates a file and opens it for writing (FileExistsError is raised when the file does exist)
'''

'''
     |  readable(...)
     |      readable() -> bool.  True if file was opened in a read mode.
     |  write(...)
     |      Returns the number of bytes written, which is never less than
     |      len(b).
     |  close(...)
     |      close() -> None.  Close the file.
     |      A closed file cannot be used for further I/O operations.  close() may be
     |      called more than once without error.
     |  detach(...)
     |      Disconnect this buffer from its underlying raw stream and return it.
     |      After the raw stream has been detached, the buffer is in an unusable
     |      state.
     |  fileno(...)
     |      fileno() -> int.  Return the underlying file descriptor (an integer).
     |  flush(...)
     |      Flush write buffers, if applicable.
     |      This is not implemented for read-only and non-blocking streams.
     |  isatty(...)
     |      isatty() -> bool.  True if the file is connected to a TTY device.
     |  readline(...)
     |  readlines(...)
     |      Return a list of lines from the stream.
     |  read(...)
     |      read(size: int) -> bytes.  read at most size bytes, returned as bytes.
     |      Return an empty bytes object at EOF.
     |  seekable(...)
     |      Return whether object supports random access.
     |      If False, seek(), tell() and truncate() will raise UnsupportedOperation.
     |      This method may need to do a test seek().
     |  seek(...)
     |   seek(offset [ , whence ] )
     |   	•SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
     |   	•SEEK_CUR or 1 – current stream position; offset may be negative
     |   	•SEEK_END or 2 – end of the stream; offset is usually negative
     |   	Return the new absolute position.
     |  tell(...)
     |      tell() -> int.  Current file position.
     |      Can raise OSError for non seekable files.
     |  truncate(...)
     |      truncate([size: int]) -> int.  Truncate the file to at most size bytes
     |      and return the truncated size.
     |  writable(...)
     |      writable() -> bool.  True if file was opened in a write mode.
     |  writelines()
'''
