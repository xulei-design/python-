# 1.一个函数作为另一个函数的参数（lambda基本上都是）
# 2.一个函数作为另一个函数的返回值
def test():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return test


def bar():
    print('我是bar函数')
    return test()


# x=test()
# print(x)

# y = demo()  # y是test函数
# print(y)
# z = y()
# print(z)

a = bar()
print(a)


# 3.函数内部再定义一个函数

def foo():
    print('我是foo，我被调用了')
    return 'foo'


def bar():
    print('我是bar，我被调用了')
    return foo


# x = bar()
# print('x的值是{}'.format(x))
#
# print('-----')
# x()


y = bar()()
print(y)


# 装饰器
def outer():
    m = 100

    def inner(): #inner 函数是定义在outer函数内部的一个函数
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    return inner


outer()()
