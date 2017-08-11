#!/usr/bin/env python3
import re
def main():
    # (...)    Matches the RE inside the parentheses.
    # "|"      A|B, creates an RE that will match either A or B.
    fileHandle = open('raven.txt', 'r')
    for line in fileHandle.readlines():
        if re.search('(Len|Neverm)ore', line):
            print(line, end = '')
    print('\n' * 3)
    fileHandle = open('raven.txt', 'r')
    for line in fileHandle.readlines():
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())
if __name__=="__main__": main()