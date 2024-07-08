# *args 表示可变位置参数
# **kwargs 表示可变的关键字参数


def add(a, b, *args, mul=1, **kwargs):  # 可变位置参数要在前，缺省参数要放到可变位置参数后面。
    # print('a={},b={}'.format(a, b))
    # print('args={}'.format(args)) # 多出来的位置参数会以元组的形式保存到args里
    print('kwargs={}'.format(kwargs)) # 多余的关键字参数会以字典的形式保存在kwargs
    # 求和
    c = a + b
    for arg in args:
        c += arg
    return c * mul


# def add(*args):
#     pass


add(1, 4)
print(add(2, 3, 4, 5, 6, mul=2, x=5, y=6))
