#!/usr/bin/env python3

# A class method takes the class (not instance) as argument
# and works with the class object
# A static method requires no argument and does not work
# with the class or instance (but it still belongs in the class code)
# A decorator is a processor that modifies a function
# @classmethod and @staticmethod modify the default binding
# that instance methods provide

class InstanceCounter(object):
	count = 0							# class attribute

	def __init__(self, val):			# instance/bound method
		self.val = self.filterint(val)
		InstanceCounter.count += 1

	def set_val(self, newval):			# instance/bount method
		self.val = newval

	def get_val(self):					# instance/bount method
		return self.val

	@classmethod
	# if we apply the classmethod decorator to a method, we can
	# call that method to pass the class automatically when called
	# instead of the instance
	def get_count(cls):					# class method
		return cls.count

	@staticmethod
	# filterint is a utility class that has nothing to do with
	# class attributes and/or instance attributes
	def filterint(value):				# static method
		if not isinstance(value, int):
			return 0
		else:
			return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter('hello')

for obj in (a, b, c, d):
	print("val of obj: %s" % (obj.get_val()))	# initialized value
	print("count: %s" % (obj.get_count()))		# always 3

print(InstanceCounter.get_count())