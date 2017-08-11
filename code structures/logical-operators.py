# Note that: 0, 0.0, False, None, '', [], {}, {}, () and any empty object are considered to be Fasle, otherwise,
# it is True
a, b = 5, 10
print("a = %d and b = %d" % (a, b))
print("Is %d > 2 and %d <= 5? %r" % (a, a, a > 2 and a <= 5))
print("Is 2 < %d < 6? %r" % (a, 2 < a < 6))
print("Is %d > %d or %d > %d? %r" % (a, b, a, b, a > b or b > a))
print("Is %d < %d and not %d < %d? %r" % (a, b, b, a, a < b and not b < a))
print("Is %d < %d <= %d < %d? %r" % (4, a, 5, 10, 4 < a <= 5 < 10))

