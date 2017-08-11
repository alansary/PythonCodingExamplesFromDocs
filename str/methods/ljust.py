# ljust()
'''
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
'''
string = "This is a string"
print("The string is '%s' and its length is %d" % (string, len(string)))
print("Left justifiying the string with spaces in width 5: '%s'" % string.ljust(5))
print("Left justifiying the string with spaces in width len(string): '%s'" % string.ljust(len(string)))
print("Left justifiying the string with spaces in width len(string) + 1: '%s'" % string.ljust(len(string) + 1))
print("Left justifiying the string with the fill character '@' in width len(string) + 10: '%s'" % string.ljust(len(string) + 10, '@'))
string = ""
print("Left justifiying the string '%s' with  the fill character 'X' in width 10, we have: '%s'" % (string, string.ljust(10, 'X')))

