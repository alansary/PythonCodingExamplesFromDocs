# islower()
'''
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
'''
string = "tHis is a string"
print("Is all cased characters in '%s' are lower? %s" % (string, string.islower()))
string = "this is a string"
print("Is all cased characters in '%s' are lower? %s" % (string, string.islower()))
string = "this @_+=-\\/a2343432"
print("Is all cased characters in '%s' are lower? %s" % (string, string.islower()))
string = ""
print("Is all cased characters in '%s' are lower? %s" % (string, string.islower()))
string = "@+==-_`1234"
print("Is all cased characters in '%s' are lower? %s" % (string, string.islower()))

