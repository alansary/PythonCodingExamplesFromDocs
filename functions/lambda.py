def test_fun(List, Func):
    for word in List:
        print(Func(word))
l = ["mohamed", "ahmed", "mahmoud"]
def my_fun(x):
    return x.capitalize() + '!'
test_fun(l, my_fun)
# lambda is just like inline function in C (This is a function that is defined in one line)
test_fun(l, lambda x: x.capitalize() + '!')
def test(l, fun):
    for x in l:
        print(fun(x, l))
test(['mohamed', 'ahmed', 'omar'], lambda x, l: len(x) * l)
