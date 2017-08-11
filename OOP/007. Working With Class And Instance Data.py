#!/usr/bin/env python3

class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = val
		InstanceCounter.count += 1

	def set_val(self, newval):
		self.val = newval

	def get_val(self):
		return self.val

	def get_count(self):
		return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
	print("val of obj: %s" % (obj.get_val()))	# initialized value
	print("count: %s" % (obj.get_count()))		# always 3

for obj in (a, b, c):
	print("val of obj: %s" % (obj.get_val()))	# initialized value
	print("count (from instance): %s" % (obj.count))	# always 3

class TestClass(object):
    pass

print(TestClass)        # class object
TestClass.val = 5       # setting an attribute of the class TestClass
print(TestClass.val)