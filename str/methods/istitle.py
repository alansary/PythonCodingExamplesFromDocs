# istitle()
'''
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
'''
# title()
'''
 |  title(...)
 |      S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
'''
	# To convert a string to a title if it contains at least one character, we can use the title() method
string = ""
print("The string '%s' is title? %s" % (string, string.istitle()))
string = "123@@@"
print("The string '%s' is title? %s" % (string, string.istitle()))
	# We can not use title() here, it can not be a title since it doesn't contain any characters
string = "This is A String"
print("The string '%s' is title? %s" % (string.title(), string.title().istitle()))
print("The string '%s' is title? %s" % (string, string.istitle()))
string = "This Is A Title"
print("The string '%s' is title? %s" % (string, string.istitle()))
string = "Th~23:@is T ''afj"
print("The string '%s' is title? %s" % (string, string.istitle()))
print("The string '%s' is title? %s" % (string.title(), string.title().istitle()))
string = "Th~23:@Is T S''Afj"
print("The string '%s' is title? %s" % (string, string.istitle()))
string = "23f@"
print("The string '%s' is title? %s" % (string, string.istitle()))
print("The string '%s' is title? %s" % (string.title(), string.title().istitle()))
string = "THis Is A String"
print("The string '%s' is title? %s" % (string, string.istitle()))
print("The string '%s' is title? %s" % (string.title(), string.title().istitle()))
string = "This Is The Script"
print("The string '%s' is title? %s" % (string, string.istitle()))
string = "234@ A"
print("The string '%s' is title? %s" % (string, string.istitle()))

