# isdecimal()
'''
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
'''
	# Decimal: 012...9
import string
print(string.digits)
string = ""
print("Is the string '%s' is decimal? %s" % (string, string.isdecimal()))
string = "1223"
print("Is the string '%s' is decimal? %s" % (string, string.isdecimal()))
string = "12.3"
print("Is the string '%s' is decimal? %s" % (string, string.isdecimal()))
string = "1 2 3"
print("Is the string '%s' is decimal? %s" % (string, string.isdecimal()))
string = "12EF"
print("Is the string '%s' is decimal? %s" % (string, string.isdecimal()))

