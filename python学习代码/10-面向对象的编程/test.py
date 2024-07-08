from greenlet import greenlet

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()

def func2():
    print(3)
    grl.switch()
    print(4)
