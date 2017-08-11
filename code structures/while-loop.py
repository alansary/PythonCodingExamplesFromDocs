a = 0
print("The even integers from 0 to 10 are:")
while a <= 10:
    if a % 2 == 0: print(a, end = ' ')
    else: pass
    a += 1
print("")
while True:
    i = input("Enter a number [q = cancel]:")
    if i == 'q': break
    elif not int(i) % 2 == 0: continue
    else: print(i)
while True:
    i = input("Enter to capitalize [q = cancel]:")
    if i == 'q': break
    else: print(i.capitalize())

