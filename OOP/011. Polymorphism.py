#!/usr/bin/env python3

# Polymorphism ("Many Shapes")
# The third pillar of OOP
# Two classes with same interface (i.e., method name)
# The methods are often different, but conceptually similar
# Duck typing refers to reading an object's attributes to decide
# whether it is of a proper type, rather than checking the type
# itself
# If it walks like a duck and it quacks like a duck, it must be a duck
# i.e., len() && __len__

class Animal(object):

	def __init__(self, name):
		self.name = name

	def eat(self, food):
		print("{0} eats {1}".format(self.name, food))

class Dog(Animal):

	def fetch(self, thing):
		print("{0} goes after the {1}!".format(self.name, thing))

	def show_affection(self):
		print("{0} wags tail".format(self.name))

class Cat(Animal):

	def swatstring(self):
		print("{0} shreds the string!".format(self.name))

	def show_affection(self):
		print("{0} purrs".format(self.name))

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
	a.show_affection()
