#!/usr/bin/env python3

# When working in a child class we can choose to
# implement parent class methods in different ways
# Inherit: simply use the parent class' defined method
# Override/overload: provide child's own version of a method
# Extend: do work in addition to that in parent's method
# Provide: implement abstract method that parent requires

import abc

class GetSetParent(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, value):
		self.val = 0
	def set_val(self, value):
		self.val = value
	def get_val(self):
		return self.val
	@abc.abstractmethod
	def showdoc(self):
		return

class GetSetInt(GetSetParent):
	# Extend (Specializing)
	def set_val(self, value):
		if not isinstance(value, int):
			value = 0
		super(GetSetInt, self).set_val(value)
	# Provide
	def showdoc(self):
		print("GetSetInt object ({0}), only accepts "
			"integer values".format(id(self)))

	# Inherit __init__ && get_val

class GetSetList(GetSetParent):
	# Override/overload
	def __init__(self, value=0):
		self.vallist = [value]
	# Override/overload
	def get_val(self):
		return self.vallist[-1]
	# Override/overload
	def get_vals(self):
		return self.vallist
	# Override/overload
	def set_val(self, value):
		self.vallist.append(value)
	# Provide
	def showdoc(self):
		print("GetSetList object, len {0}, stores "
			"history of values set".format(self.vallist))

x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()

