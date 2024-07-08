# with 语句后面的结果对象，需要重写 __enter__ 和 __exit__方法
# 当进入到 with 代码块时，会自动调用 __enter__ 方法里的代码
# 当 with 代码块执行完成以后，会自动调用 __exit__ 方法
class Demo(object):

    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


def creat_obj():
    x = Demo()
    return x

# 都需要创建对象去自动调用
# d = creat_obj().__enter__()
# 使用with 首先会创建一个对象 n = creat_obj(),和open 函数类似
# with open('01-打开文件.py','r',encoding='utf8') as m:
with creat_obj() as d: # as 变量名, d 是一个对象类型，而不是类
    # 变量d 不是creat_obj 的返回结果，
    # 它是创建的对象 x 自动调用 __enter__ 之后的返回结果
    print(d)
