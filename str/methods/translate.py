# translate()
'''
 |  translate(...)
 |      S.translate(table) -> str
 |      
 |      Return a copy of the string S in which each character has been mapped
 |      through the given translation table. The table must implement
 |      lookup/indexing via __getitem__, for instance a dictionary or list,
 |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
 |      this operation raises LookupError, the character is left untouched.
'''
# maketrans()
'''
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.
'''
string = "Mohamed Amr Mohamed Nagib Alansary"
dictionary = {'M':'ThisIsM', 'A':None, 'o':'X'}
oneArgTransTable = string.maketrans(dictionary)
string1 = "MAo"
string2 = "t X"
twoArgTransTable = string.maketrans(string1, string2)
string3 = "h"
threeArgTransTable = string.maketrans(string1, string2, string3)
print(string)
print("First Transition:")
print("Transitions ->\t'M':'ThisIsM', 'A':None, 'o':'X'")
print(string.translate(oneArgTransTable))
print("Second Transition:")
print("Transitions ->\t'M':'t', 'A':' ', 'o':'X'")
print(string.translate(twoArgTransTable))
print("Third Transition:")
print("Transitions ->\t'M':'t', 'A':' ', 'o':'X', 'h':None")
print(string.translate(threeArgTransTable))

