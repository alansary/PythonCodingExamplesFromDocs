# rpartition()
'''
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
'''
string = "This is a string"
print("Partitioning the string '%s' with '%s' as a separator, we have: '%s'" % (string, ' is ', string.partition(' is ')))
print("Partitioning the string '%s' with '%s' as a separator, we have: '%s'" % (string, 'lssl', string.partition('lssl')))

