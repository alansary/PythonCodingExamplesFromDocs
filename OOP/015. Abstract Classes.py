#!/usr/bin/env python3

# Abstract Base Classes
# An abstract class is a kind of "model" for other classes to
# be defined. it is not designed to construct instances, but
# can be subclassed by regular classes
# Abstract classes can define an interface, or methods that
# must be implemented by its subclasses
# This is a contract that an subclassed class must follow
# The python abc module enables the creation of abstract base classes

import abc

class GetterSetter(object):
	# assigning abc.ABCMeta to the magic attribute __metaclass__
	# defines the class GetterSetter as an abstract base class
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def set_val(self, input):
		"""Set a value in the instance."""
		return

	@abc.abstractmethod
	def get_val(self):
		"""Get and return a value from the instance."""
		return

class MyClass(GetterSetter):

	def set_val(self, input):
		self.val = input

	def get_val(self):
		return self.val

x = MyClass()
print(x)