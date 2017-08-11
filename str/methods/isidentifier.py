# isidentifier()
'''
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
'''
	# Identifiers: are the names of the variable, functions, modules, objects, classes and keywords.
print("Is syntactically valid")
identifier = "firstvar"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "1stvar"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "_first_var"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "first var"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "for"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "first~var"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "while"
print(identifier, identifier.isidentifier())
print("Is syntactically valid")
identifier = "import"
print(identifier, identifier.isidentifier())
   
