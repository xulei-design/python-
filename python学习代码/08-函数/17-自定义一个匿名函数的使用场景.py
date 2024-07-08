# 第二种调用匿名函数的使用方式
# 把这个函数当作参数传给另一个函数使用（使用场景比较多）重点理解
# 在函数中不固定的地方加参数
def calc(a, b, fn):
    c = fn(a, b)
    return c


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


# 回调函数
x1 = calc(1, 2, add) # a=1 b=2 fn=add
print(x1)
x2 = calc(10, 5, minus) # a=10 b=5 fn=minus
print(x2)


x3 = calc(5, 7, lambda x, y: x + y) #x=5 y=7 然后调用匿名函数拿到参数算法进行计算
x4 = calc(19, 3, lambda x, y: x - y)
x5 = calc(2, 7, lambda x, y: x * y)
x6 = calc(12, 3, lambda x, y: x / y)
print(x3, x4, x5, x6)