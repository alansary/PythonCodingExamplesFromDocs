#!/usr/bin/env python3
import re
'''
        \.       Matches the dot character
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        re.X
        re.VERBOSE
            This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually
            separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a
            character class or when preceded by an unescaped backslash. When a line contains a # that is not in a character class and
            is not preceded by an unescaped backslash, all characters from the leftmost such # through the end of the line are ignored.
'''
def main():
    test_list = ['2.34', '23', '23.10', '2.0', '13.0', '12.', '.12']
    # The following pattern means starts with one or more decimal digit followed by a period then zero or more decimal digit
    pattern = re.compile(r"""\d +  # the integral part
        \.    # the decimal point
        \d *  # some fractional digits""", re.X)
    for line in test_list:
        if re.search(pattern, line):
            print(line)
    print('\n' * 3)
    pattern = re.compile(r'\d+\.\d*')
    for line in test_list:
        if re.search(pattern, line):
            print(line)
    print('\n' * 3)
    '''
    '.'
    (Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any
    character including a newline.
    '''
    test_list = ['this is a string', 'this is a line', 'this is the strong', 'this is the second line']
    pattern = re.compile(r'.tr.ng')
    for line in test_list:
        if re.search(pattern, line):
            print(line)
    print('\n' * 3)
    fh = open('work.txt')
    pattern = re.compile(r'''. # Matches any character except \n
        * # Matches 0 or more (greedy) repetitions of the preceding RE
        in # Matches the string 'in'
        .   # Matches any character except \n
        ''', re.VERBOSE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end = '')
    print('\n' * 3)
    fh.seek(0, 0)
    pattern = re.compile(r'.*in..')
    for line in fh:
        if re.search(pattern, line):
            print(line, end = '')
    print('\n' * 3)
    '''
    re.S
    re.DOTALL
    Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except
    a newline.
    '''
    fh.seek(0, 0)
    pattern = re.compile(r'.*in..', re.DOTALL)
    for line in fh:
        if re.search(pattern, line):
            print(line, end = '')
    print('\n' * 3)
if __name__=="__main__": main()