# count()
'''
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
'''
t = (1, 2, 2, 1, 1, 1, 3, 4, 3, 1)
print("The tuple of values is %r" % (t,)) # If you put % t without the parentheses, it will substitute (1, 2, 2, 1, 1, 1, 3, 4, 3, 1) for t (Error)
					  # Putting a comma at the end indicates that this is a tuple that contains one element which is the tuple t
					  # Note that: without the ',' it will interpret it as ((1, 2, 2, 1, 1, 1, 3, 4, 3, 1)) (Error)
print("The number of occurrences of '1' in the tuple %r is %d" % (t, t.count(1)))
print("The number of occurrences of '0' in the tuple %r is %d" % (t, t.count(0)))

