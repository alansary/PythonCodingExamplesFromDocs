#!/usr/bin/env python3

import random

class MyClass(object):
	def doThis(self):
		self.rand_val = random.randint(1, 10)

myInst = MyClass()
myInst.doThis()
print(myInst.rand_val)