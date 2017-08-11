#!/usr/bin/env python3
import re
def main():
    fh = open('raven.txt', 'r')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(re.sub('(Len|Neverm)ore', '###', line), end = '')
    print('\n' * 3)
    fh.seek(0, 0)
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end = '')
if __name__=="__main__": main()