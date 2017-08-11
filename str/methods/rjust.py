# rjust()
'''
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
'''
string = "This is a string"
print("The string is '%s' and its length is %d" % (string, len(string)))
print("Right justifiying the string with spaces in width 5: '%s'" % string.rjust(5))
print("Right justifiying the string with spaces in width len(string): '%s'" % string.rjust(len(string)))
print("Right justifiying the string with spaces in width len(string) + 1: '%s'" % string.rjust(len(string) + 1))
print("Right justifiying the string with the fill character '@' in width len(string) + 10: '%s'" % string.rjust(len(string) + 10, '@'))
string = ""
print("Right justifiying the string '%s' with  the fill character 'X' in width 10, we have: '%s'" % (string, string.rjust(10, 'X')))

