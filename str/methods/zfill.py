# zfill()
'''
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
'''
	# zfill(width) == rjust(width, '0')
string = ""
print("The empty string '%s' zfilled, width = 1 is '%s'" % (string, string.zfill(1)))
string = "This is a string"
print("The string '%s' zfilled, width = len(string) is '%s'" % (string, string.zfill(len(string))))
print("The string '%s' zfilled, width = len(string) + 1 is '%s'" % (string, string.zfill(len(string)+1)))
print("The string '%s' zfilled, width = len(string) + 1 (rjust() method) is '%s'" % (string, string.rjust(len(string)+1, '0')))

