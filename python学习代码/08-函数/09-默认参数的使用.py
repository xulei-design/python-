def say_hello(name, age, addr="襄阳"):  # 形参addr设置了一个默认值
    print('大家好，我的名字是{}，我今年{}岁了，我来自{}'.format(name, age, addr))
say_hello('朱海涛', 19)  # 如果没有传递参数，会使用默认值
say_hello('许磊', 19, '河南')  # 如果传递参数，就使用传递的实参

# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('jerry', age=18, addr='南京') #可以直接传递单个参数，也可以使用变量赋值进行行参的传递

# 缺省参数：要放在最后面，关键字参数
# 有些函数的参数是，如果你传递了参数，就使用参数，
# 如果没有传递参数，就使用默认值


# print函数里end就是一个缺省参数
# print('hello',end='')
# print('world')

print('hello', '你好', sep='____')
