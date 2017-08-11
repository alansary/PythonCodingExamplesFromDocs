# format()
'''
format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
'''
x, y = 1, 2
print("{0}, {1}".format(x, y))
print("{1}, {0}".format(x, y))
print("{0}{1}{0}".format("abra", "cad")) # These numbers represents the order (positional order in the format method)
print("{BlaBla} {BlaBlaBla}".format(BlaBla = x, BlaBlaBla = y))
d = dict(BlaBla = x, BlaBlaBla = y)
print(d)
print("{BlaBlaBla} {BlaBla}".format(**d)) # This double asterisk refers to the dictionary
print("{a}, {b}".format(b = 12, a = (1, 2, 3))) # Named Arguments
print("{}, {a}".format(x, a = 12))
print("{}, {}".format(y, x))
string = "The first number: {} and the second number {}"
print(string, string.format(x, y), string.format(y, x))
s = {1, 2, 3}
print("{}, {} and {}".format(*s)) # Scatter
l = [1, 2, 3]
print("{} and {}".format(*l)) # Scatter
r = range(4)
print("{3} and {2}".format(*r)) # Scatter
