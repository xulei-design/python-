# 有很多可迭代对象: list tuple dict set range filter map
# for...in 可迭代对象
from collections.abc import Iterable
# class Foo(object):
#     def __next__(self):
#         return 1


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0
    def __iter__(self): # 只要重写了 __iter__ 方法就是一个可迭代对象
        # return Foo()
        return self  # 返回对象是自己
    def __next__(self):
        # 每一次 for...in都会调用一次 __next__方法,获取返回值
        self.count += 1
        if self.count <= self.x:
            return self.count-1
        else:
            raise StopIteration # 抛出一个错误,让迭代器停止


d = Demo(10)
# isinstance:用来判断一个实例对象是否是由一个指定的类创建出来的
print(isinstance(d, Iterable)) # True
# for...in..循环本质就是调用可迭代对象的__iter__方法,获取到这个方法的返回值
# 这个返回值需要是一个迭代器对象,然后再调用这个对象的__next__方法
for x in Demo(10):
    print(x)


names = list(('zhangsan', 'lisi'))
print(isinstance(names, Iterable)) # True
a = int('123')

# for i in range(10):
#     print(i)
