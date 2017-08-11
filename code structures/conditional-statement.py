a, b = 0, 1
print('foo' if a < b else 'bar')
x = 'foo' if a < b else 'bar'
print(x)
def test_fun1(a, b):
    if a:
        if not b:
            print("a is True and b is False")
        else:
            print("a is True and b is True")
    else:
        if b:
            print("b is True and a is False")
        else:
            print("b is False and a is False")
test_fun1(True, True)
test_fun1(True, False)
test_fun1(False, True)
test_fun1(False, False)
def test_fun2(x):
    print("The name is %s" % x)
    if x == "Ahmed":
        print("He is Ahemd")
    elif x == "Amr":
        print("He is Amr")
    elif x == "Mohamed":
        print("He is Mohamed")
    else:
        print("I cannot identify his identitiy")
test_fun2("Mohamed")
test_fun2("Ahmed")
test_fun2("Amr")
test_fun2("Anonymous")

