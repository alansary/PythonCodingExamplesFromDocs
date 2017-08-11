#!/usr/bin/env python3

class MyClass(object):
	# setter method
	def set_val(self, val):
		self.value = val

	# getter method
	def get_val(self):
		return self.value

# Encapsulation: the first of the three pillars of OOP
# Data should be accessed only through instance methods
# Data should be validated as correct
# Data should be save from changes by external processes

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())

a.value = "Hello"
print(a.get_val())

class MyInteger(object):
	def set_val(self, val):
		try:
			val = int(val)
		except ValueError:
			return
		self.val = val

	def get_val(self):
		return self.val

	def increment_val(self):
		self.val += 1

i = MyInteger()
i.set_val(9)
print(i.get_val())
i.set_val('hi')
print(i.get_val())
i.val = 'hi'
try:
    i.increment_val()
except TypeError as err:
    print(err)
