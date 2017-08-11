#!/usr/bin/env python
from sources import daily, weekly
print("The daily weather is %s" % daily.forecast())
print("The weekly weather is:")
for i, outlook in enumerate(weekly.forecast(), 1):
    print(i, outlook)
print("The weekly weather is:")
for i, outlook in zip(range(1, 100), weekly.forecast()):
    print(i, outlook)
print(daily.sayHello)
