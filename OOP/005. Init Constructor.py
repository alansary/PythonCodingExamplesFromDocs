#!/usr/bin/env python3

# __init__ is a private/magic method that is intended to use
# internally, not called by the user of the class, magic methods
# are called automatically when a particular event happens
# __init__ is called when instantiating a new object of the class

class MyNum(object):
	def __init__(self):
		print('calling __init__ MyNum')
		self.val = 0

	def increment(self):
		self.val = self.val + 1

dd = MyNum()		# calling __init__
dd.increment()
dd.increment()
print(dd.val)		# 2

class MyNum2(object):
    def __init__(self, value):
        print('calling __init__ MyNum2')
        self.val = value

    def increment(self):
        self.val = self.val + 1

dd = MyNum2(5)      # calling __init__
dd.increment()
dd.increment()
print(dd.val)       # 7
dd2 = MyNum2('hi')
try:
    dd2.increment()
except TypeError as err:
    print(err)

class MyNum3(object):
    def __init__(self, value):
        print('calling __init__ MyNum3')
        self.val = 0
        self.correct_val = False
        self.value = value
        try:
            value = int(value)
            self.val = value
            self.correct_val = True
        except ValueError as err:
            print(err)

    def increment(self):
        if (self.correct_val):
            self.val = self.val + 1
        else:
            print('invalid literal for int() with base 10: \'{}\''.format(self.value))

dd = MyNum3(5)
dd.increment()
dd.increment()
print(dd.val)
dd2 = MyNum3('hi')
dd2.increment()
dd2.increment()
print(dd2.val)

class MyNum4(object):
	def __init__(self, value=0):
		print('calling __init__ MyNum4')
		self.val = value

	def increment(self):
		self.val = self.val + 1

dd = MyNum4()		# calling __init__
dd.increment()
dd.increment()
print(dd.val)		# 2
dd2 = MyNum4(5)      # calling__init__
dd2.increment()
dd2.increment()
print(dd2.val)      # 7