# center()
'''
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
'''
string = "This is a string"
print("The string is '%s'" % string)
print("Centering the string and enclosing it within '@' signs: '%s'" % string.center(len(string)+3, '@'))
print("Centering the string and enclosing it within '@' signs: '%s'" % string.center(len(string)+4, '@'))
print("The default fill char is a space: '%s'" % string.center(len(string)+10))
