#!/usr/bin/env python3

# Inheritance: the second pillar of OOP
# Object.Attribute Lookup Hierarchy
# The instance
# The class
# Any class from which this class inherits

# An inheriting/child/derived/subclass class
# An inherited/parent/base/superclass class

class Date(object):		# inherits from the 'object' class
	def get_date(self):
		return '2014-10-13'

class Time(Date):		# inherits from the 'Date' class
	def get_time(self):
		return '08:13:07'

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())	# found this method in the 'Date' class