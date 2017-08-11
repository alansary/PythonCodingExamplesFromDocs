# expandtabs()
'''
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
'''
string = "This\tis\ta\tstring"
print("The string is '%s'" % string)
print("The raw representation of the string is '%s'" % repr(string))
print("The string with tabs expanded and tabsize is the default size (8) is '%s'" % string.expandtabs())
print("The string with tabs expanded and tabsize is the space size (1) is '%s'" % string.expandtabs(1))
print("The string with tabs expanded and tabsize is 4 is '%s'" % string.expandtabs(4))

