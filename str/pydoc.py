'''
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
Characteristics
 |      Strings are immutable and indexed.
Methods
 |      S.capitalize() -> str
 |      S.casefold() -> str
 |      S.center(width[, fillchar]) -> str
 |      S.count(sub[, start[, end]]) -> int
 |      S.index(sub[, start[, end]]) -> int
 |      	Like S.find() but raise ValueError when the substring is not found.
 |      S.isalnum() -> bool
 |      S.isalpha() -> bool
 |      S.isdecimal() -> bool
 |      S.isdigit() -> bool
 |      S.isidentifier() -> bool
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      S.islower() -> bool
 |      S.isnumeric() -> bool
 |      S.isprintable() -> bool
 |      	Return True if s is empty as well
 |		' ', and \t are printable
 |      S.isspace() -> bool
 |      S.istitle() -> bool
 |      S.isupper() -> bool
 |      S.join(iterable) -> str
 |      S.ljust(width[, fillchar]) -> str
 |      S.lower() -> str
 |      S.lstrip([chars]) -> str
 |      S.partition(sep) -> (head, sep, tail)
 |      S.replace(old, new[, count]) -> str
 |      S.rfind(sub[, start[, end]]) -> int
 |      S.rindex(sub[, start[, end]]) -> int
 |      S.rjust(width[, fillchar]) -> str
 |      S.rpartition(sep) -> (head, sep, tail)
 |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      S.rstrip([chars]) -> str
 |      S.split(sep=None, maxsplit=-1) -> list of strings
 |      S.splitlines([keepends]) -> list of strings
 |      	\n, \r, \v, \x0b, and \x0c are line boundaries
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      	prefix can also be a tuple of strings to try.
 |      S.strip([chars]) -> str
 |      S.swapcase() -> str
 |      S.title() -> str
 |      S.translate(table) -> str
 |      S.upper() -> str
 |      S.zfill(width) -> str
 |      	Equivalent to rjust(width, '0')
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      One argument   : Dict -> {ord|char:ord|str|None}
 |	Two arguments  : len(str1) == len(str2) s.t. c11:c21, c12:c22, ..., c1n:c2n
 |	Three arguments: str3 chars are mapped to None
 |
Last Methods
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      	suffix can also be a tuple of strings to try.
 |      S.expandtabs(tabsize=8) -> str
 |      S.find(sub[, start[, end]]) -> int
 |      	Return -1 on failure.
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
'''
