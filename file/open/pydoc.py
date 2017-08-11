'''
open(...)
    open(file, mode='r', buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None) -> file object 
    Open file and return a stream.  Raise IOError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
Modes:
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    locale.getpreferredencoding(False) -> Current locale encoding ('UTF-8')
    For reading and writing raw bytes use binary mode and leave encoding
    unspecified.

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.

    in binary mode return contents as bytes objects without any decoding.
    in text mode the contents of the file are returned as strings, the bytes 
    having been first decoded using a platform-dependent encoding or using
    the specified encoding if given.

    run 'help(codecs.Codec)' for a list of the permitted encoding error strings.

    text mode ('w', 'r', 'wt', 'rt', etc.), it returns a TextIOWrapper
    in a binary mode, the returned class varies:
        in read binary mode, it returns a BufferedReader
        in write binary and append binary modes, it returns a BufferedWriter
    read/write mode, it returns a BufferedRandom.

    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
'''

