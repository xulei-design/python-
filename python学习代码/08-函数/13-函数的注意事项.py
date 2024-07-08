# 函数的三要素：函数名，参数和返回值
# 在有一些编程语言里，允许函数重名，在python里不允许函数重名
# 如果函数重名了，后一个函数会覆盖前一个函数

# def test(a, b):
#     print('hello,a={},b={}'.format(a, b))

# test = 对应一个函数
def test(x):
    print('good,x={}'.format(x))


test(3)

# python里，函数名也可以理解为一个变量名

input = 5
