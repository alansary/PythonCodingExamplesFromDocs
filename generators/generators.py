#!/usr/bin/python3
# We can make a generator using tuples with comprehension
test_tuple = ()
print("%r is a %r" % (test_tuple, type(test_tuple)))
generator = (n for n in range(1, 11, 1))
print("%r is a %r" % (generator, type(generator)))
print("Looping through this generator, its elements are:")
for e in generator:
    print(e, end = ' ')
print("")

# We can also use function definition to make a generator
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
# primes is the generator, what yield does is that it returns the value n and the next time it is called it continues execution at the
# next line, then continues to the next iteration
def primes(n = 1):
   while(True): # infinitely appends elements to the generator
       if isprime(n): yield n # if the number is prime, then append it to the generator primes()
       n += 1 # will execute if we yield n executed or yield n doesn't execute, then goes to the next iteration

for n in primes(): # n is the appended element in the generator primes
    if n > 100: break # check the number n in the generator
    print(n) # if n <= 100 print it

def isodd(n):
    if n % 2 == 0: return False
    else: return True
def odds(n=1):
    while True:
        if isodd(n): yield n
        n += 1
for i in odds():
    if i > 100:
        break
    print(i)
'''
def inclusive_range(*args):
    if len(args) < 1: raise TypeError('inclusive_range expected 1 arguments, got {}'.format(len(args)))
    elif len(args) == 1:
        start = 0
        stop = args[0]
        while start <= stop:
            yield start
            start += 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        if not start >= stop:
            while start <= stop:
                yield start
                start += 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step_size = args[2]
        if start <= stop:
            while start <= stop:
                yield start
                start += step_size
        else:
            while start >= stop:
                yield start
                start += step_size
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(len(args)))
'''
'''
def inclusive_range(*args):
    if len(args) < 1: raise TypeError('inclusive_range expected 1 arguments, got {}'.format(len(args)))
    elif len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(len(args)))
    if start > stop and len(args) == 3 and step < 0:
        while start >= stop:
            yield start
            start += step
    elif start > stop and len(args) == 3 and step >= 0:
        return
    else:
        while start <= stop:
            yield start
            start += step
for x in inclusive_range(10):
    print(x, end = ' ')
print()
for x in inclusive_range(0, 10):
    print(x, end = ' ')
print()
for x in inclusive_range(10, 0):
    print(x, end = ' ')
print()
for x in inclusive_range(1, 99, 2):
    print(x, end = ' ')
print()
for x in inclusive_range(100, 0, -2):
    print(x, end = ' ')
print()
# for x in inclusive_range():
#     print(x, end = ' ')
# print()
for x in inclusive_range(10, 20, 30, 40):
    print(x, end = ' ')
'''
# SyntaxError: non-default argument follows default argument
# def inclusive_range2(start = 0, stop, step = 1):
#     while start <= stop:
#         yield start
#         start += step


def irange(*args):
    # assert len(args) >= 1 and len(args) <= 3, 'irange expected at least 1 argument and at most 3 arguments, got {}'.format(len(args))
    if len(args) < 1: raise TypeError('irange expected 1 arguments, got {}'.format(len(args)))
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else: raise TypeError('irange expected at most 3 arguments, got {}'.format(len(args)))
    if start > stop and len(args) == 3 and step < 0:
        while start >= stop:
            yield start
            start += step
    elif start > stop and len(args) == 3 and step >= 0:
        return
    else:
        while start <= stop:
            yield start
            start += step
for x in irange(10):
    print(x, end = ' ')
print()
for x in irange(0, 10):
    print(x, end = ' ')
print()
for x in irange(10, 0):
    print(x, end = ' ')
print()
for x in irange(1, 99, 2):
    print(x, end = ' ')
print()
for x in irange(100, 0, -2):
    print(x, end = ' ')
print()
for x in irange(10, 0, 2):
    print(x, end = ' ')
print()
# for x in range()
# for x in range(10, 20, 30, 40)

