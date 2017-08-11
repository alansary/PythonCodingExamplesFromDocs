# Multiple Inheritance
# depth-first or breadth-first?
# Python will use a depth-first search for an attribute

class A(object):

	def dothis(self):
		print("dothis A class (Grand Parent Class)")

class B(A):
	pass

class C(object):

	def dothis(self):
		print("dothis C class (Parent Class)")

class D(B, C):
	pass

d_inst = D()
d_inst.dothis()

# which dothis() will it call? method resolution order: D-B-A-C

print(D.mro())

# Multiple Inheritance ("diamond shape" inheritance: ambiduous!)
class A2(object):
	def dothis(self):
		print("dothis A class (Grand Parent Class)")

class B2(A2):
	pass

class C2(A2):
	def dothis(self):
		print("dothis C class (Parent Class)")

class D2(B2, C2):
	pass

d_inst2 = D2()
d_inst2.dothis()

# which dothis() will it call? method resolution order: D-B-C-A
# instead of D-B-A-C-A that looks up in A twice
# it removes the early occurrence of A

print(D2.mro())

# it is not a breadth first search, it is a depth first search with
# an additional rule, if the same class appears in a method resolution
# order, the earlier occurrences of this class are removed from
# the method resolution order

# The above applies to "new style" classes (inheriting from object)
