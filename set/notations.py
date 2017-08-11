'''
a - b (Difference)
a ^ b (Symmetric Difference)
a & b (Intersection)
a | b (Union)
a <= b (Subset)
a < b (Proper Subset)
a >= b (Superset)
a > b (Proper Superset)
'''
first_set = {1, 2, 3}
second_set = {1, 3, 4}
print("The first set is %r and the second set is %r" % (first_set, second_set))
print("The difference %r - %r is %r" % (first_set, second_set, first_set-second_set))
print("The difference %r - %r is %r" % (second_set, first_set, second_set-first_set))
print("The symmetric difference %r ^ %r is %r" % (first_set, second_set, first_set^second_set))
print("The intersection %r & %r is %r" % (first_set, second_set, first_set&second_set))
print("The union %r | %r is %r" % (first_set, second_set, first_set|second_set))
a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
print("The first set is %r and the second set is %r" % (a, b))
print("Is %r is a subset of %r? %r" % (a, b, a <= b))
print("Is %r is a subset of %r? %r" % (b, a, b <= a))
print("Is %r is a proper subset of %r? %r" % (a, b, a < b))
print("Is %r is a proper subset of %r? %r" % (b, a, b < a))
print("Is %r is a superset of %r? %r" % (a, b, a >= b))
print("Is %r is a superset of %r? %r" % (b, a, b >= a))
print("Is %r is a proper superset of %r? %r" % (a, b, a > b))
print("Is %r is a proper superset of %r? %r" % (b, a, b > a))

