#!/usr/bin/env python3

import sys
import os
import urllib.request
import random
import datetime

print(sys.version_info)
print(sys.platform)
print(os.name)
print(os.getenv('PATH'))
print(os.getcwd())
try:
    page = urllib.request.urlopen('http://www.google.com')
    for line in page:
        print(str(line), encoding = 'utf_8', end = '')
except urllib.error.URLError as e:
    print(e)
print(random.randint(1, 1000))
l = [1, 2, 3, 4, 5]
print(random.shuffle(l))
print(l)
print(datetime.datetime.now())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print('{} {} {} {} {} {} {}'.format(
    datetime.datetime.now().year,
    datetime.datetime.now().month,
    datetime.datetime.now().day,
    datetime.datetime.now().hour,
    datetime.datetime.now().minute,
    datetime.datetime.now().second,
    datetime.datetime.now().microsecond
))

# Third-Party Modules
    # http://pypi.python.org/pypi
        # Python Package Index
