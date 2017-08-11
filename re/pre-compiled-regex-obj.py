#!/usr/bin/env python3
import re
def main():
    fh = open('raven.txt', 'r')
    pattern = re.compile('(Len|Neverm)ore') # Pre-compiled regular expression object
    # This compiles the regex only once rather than compiling it every iteration through the loop
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(re.sub(pattern, '###', line), end = '')
    print('\n' * 3)
    # This also allow us to use other regex features
    fh.seek(0, 0)
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE) # This ignores case sensitivity
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(pattern.sub('###', line), end = '')
            # Or print(re.sub(pattern, '###', line), end = '')
if __name__=="__main__": main()