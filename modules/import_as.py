import random as rnd
test_list = list(range(1, 101))
print("The list is %r" % test_list)
while True:
    x = input("Press enter to get a random selection, 'q' to quit:")
    if x.lower() == 'q': break
    else:
        print("%d is a random number from the list" % rnd.choice(test_list))

