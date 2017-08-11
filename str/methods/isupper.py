# isupper()
'''
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
'''
string = "ThIS IS A STRING"
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
string = "THIS IS A STRING"
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
string = "THIS @_+=-\\/A2343432"
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
string = ""
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
string = "@+==-_`1234"
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
string = "@+==-_'1234A"
print("Is all cased characters in '%s' are upper? %s" % (string, string.isupper()))
