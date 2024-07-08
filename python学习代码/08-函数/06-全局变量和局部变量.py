a = 100  # 这个变量是全局变量，在整个py文件里都可以访问
word = '你好'


def test():
    x = 'hello'  # 这个变量时在函数内部定义的变量，他是局部变量，只能在函数内部使用
    print('x={}'.format(x))

    # 如果局部变量的名和全局变量同名，会在函数内部定义一个新的局部变量
    # 而不是修改全局变量
    a = 10  # 在函数内部有定义了一个新的局部变量
    print('函数内部a={}'.format(a))

    # 在函数内部如何修改全局变量？
    # 使用global对变量进行声明，可以通过函数修改全局变量的值
    global word
    word = 'ok'
    print('locals={},globals={}'.format(locals(), globals()))
    print(locals())


# 没有返回值的函数，调用函数就能输出，有返回值的函数，需要调用print函数才能输出
test()
# print(x)  # x只能在函数内部使用
print('函数外部a={},word={}'.format(a, word))

# 内置函数 globals()  可以查看全局变量, locals()查看局部变量

# 在 python里，只有函数能够分割作用域
if 3 > 2:
   m = 'hi'
print(m)