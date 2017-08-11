#!/usr/bin/env python3

class YourClass(object):
	classy = 10				# class attribute

	def set_val(self):
		self.insty = 100	# instance attribute

dd = YourClass()
dd.set_val()
print(dd.classy)
print(dd.insty)

# Attribute lookup order
# When we use the syntax object.attribute, we're asking Python to
# look up the attribute
# First in the instance
# Then in the class
# Method calls through the instance follow this lookup

class YourClass2(object):
	classy = 'class value!'

dd = YourClass2()
print(dd.classy)			# read classy from the class
dd.classy = 'inst value!'	# setting the value for this instance
print(dd.classy)
del dd.classy				# return the value of the class attribute
print(dd.classy)