# format_map()
'''
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
'''

print('{name} was born in {country}'.format(name='Guido', country = 'Egypt'))
# Keys must be strings (At least the ones we will use in the format string
People = {
    'name': ['Mohamed', 'john', 'peter'],
    'age': [23, 56],
}
print("My name is {name[0]},i am {age} old".format_map(People))

x, y = 1, 2
d = dict(BlaBla = x, BlaBlaBla = y)
print(d)
print("{BlaBlaBla} {BlaBla}".format(**d)) # This double asterisk refers to the dictionary