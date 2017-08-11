#!/usr/bin/env python3

# Encoding the characters with the unicode XML entities we will be able to see them

# bytes (immutable) and bytearrays (mutable) are like any container but rather than containing objects, they contain bytes
# bytes are 8-bit words of data (can hold up to 256 different values)
# This is convenient for converting strings and other binary staff

# Opening the file and read it as utf_8 and ignore whatever the default encoding is on the system
# utf_8 is a version of unicode that works in 8-bit encoding scenario
# The first 127 characters of it works exactly like ascii does (you can set your encoding to utf_8 safely)
# It will work just fine with normal ascii code (most web browsers handle utf_8 just fine)
fin = open('utf8.txt', 'r', encoding = 'utf_8')

# Opening the output file
# We will name it with the extension .html because we will open it in the browser (no html code will be written here)
fout = open('utf8.html', 'w')

# Setup a bytearray called outbytes using the bytearray() constructor
# bytearray() is a mutable list of bytes
outbytes = bytearray()

# Iterating through the file
# The ord() built-in function (ordinal) gives us the integer equivalent of the character passed to it
# There are 128 characters in utf_8 that are just normal ascii 0-127
# We will create a bytes object (immutable array of bytes)
# I'm going to encode a string, the constructor of bytes will accept the string and the encoding
# The string will be an XML entity (in the form '&#0000;' and instead of 0000 there will be a decimal value that will
# be interpreted as utf-16 which is the normal unicode)
# We will use the format {:04d} where d represents decimal
for line in fin:
    for c in line:
        if ord(c) > 127:
            # Representing the ordinal of the character into the form of XML entity and encode it with utf_8
            # We used :04d (interpreted as utf-16 which is the normal unicode)
            # We will then encode this utf-16 with utf_8
            # :04d means four decimal digits (2 * 2 * 2 * 2 == 16)
            # utf_8 is the unicode encode schema
            outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8') # Concatenating with a list
        else:
            outbytes.append(ord(c))
# If the character is outside of the normal ascii range, we are going to encode it with the shown XML entity
# which is in turn can be used in html context and that allow us to display our fancy characters
# Otherwise, we just append it to our outbytes bytearray
# Now we have our outbytes bytearray which have all characters from our string

# Turning the outbytes bytearray into a string
# We will call it outstr, and we will use the string constructor str()
outstr = str(outbytes, encoding = 'utf_8')

# Printing it to our out file
print(outstr, file = fout)

# Printing it to the screen so we can see it
print(outstr)

# This will read our utf_8 text from our file which we were not be able to read on our operating system
# This will read our utf_8 text and it will read it with utf_8 encoding
# It will write it to our utf_8 html file
# For the characters that are outside of the normal ascii range, it is going to be replaced with an XML entity

# All the characters in the file get converted to utf-16 and the printed values are the unicode values for each of them