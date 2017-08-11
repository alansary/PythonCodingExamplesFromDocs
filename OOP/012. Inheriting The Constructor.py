#!/usr/bin/env python3

# __init__ is like any other method; it can be inherited
# If a class does not have an __init__ constructor, Python
# will check its parent class to see if it can find one
# We can use the super() function to call methods in the
# parent class

import random

class Animal(object):

	def __init__(self, name):
		self.name = name

	def eat(self, food):
		print("%s is eating %s." % (self.name, food))

class Dog(Animal):

	def __init__(self, name):
		# super relates a class to its superclass
		# get the superclass of Dog and pass the Dog instance to the
		# constructor __init__; that is, we are calling Animal __init__
		# with the Dog object
		# Animal.__init__(self, name)
		super(Dog, self).__init__(name)
		self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

	def fetch(self, thing):
		print("%s goes after the %s!" % (self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)