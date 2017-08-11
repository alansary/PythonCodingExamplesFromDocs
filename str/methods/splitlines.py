# splitlines()
'''
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
'''
    # \n, \v, \r, \x0b, and \x0c are line boundaries.
string = ""
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))
string = "This is a string"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))
string = "One\nTwo\nThree"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))
string = "One\nTwo\nThree"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines(True)))
string = "One\tTwo\t\nThree\vFour"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))
string = "\nOne\x0bTwo\x0cThree\nFour\vFive"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))
string = "One\rTwo"
print("Split the string '%r' on lines, we have: '%r'" % (string, string.splitlines()))

