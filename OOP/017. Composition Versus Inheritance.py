#!/usr/bin/env python3

import random
from io import StringIO

# Composition vs. Inheritance
# Inheritance can be brittle (a change may require
# changes elsewhere)
# The composition approach uses independent classes that can
# work together but are not related in any particular way
# Decoupled code is classes, functions, etc. that work
# independently and don't depend on one another
# As long as the interface is maintainded, interactions
# between classes will work
# Not checking or requiring particular types is polymorphic
# and Pythonic
# Use two or more classes that are not related by inheritance
# but they can work together

class WriteMyStuff(object):

	def __init__(self, writer):
		self.writer = writer

	def write(self):
		write_text = "this is a silly message"
		self.writer.write(write_text)

# file class writes to files
# file handle
fh = open("017. Composition Versus Inheritance.txt", 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

# StringIO class writes to a string buffer
# string buffer is just a string that we can write to as
# if it is a file
# StringIO object
sioh = StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print("file object: ", open("017. Composition Versus Inheritance.txt", "r").read())
print("StringIO object: ", sioh.getvalue())
