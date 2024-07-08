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
# print(d.__iter__().__next__())
# i = d.__iter__()
# i.__next__()
i = iter(d) #  内置函数 iter 可以获取带一个可迭代对象的迭代器
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# 迭代器就是__iter__方法的返回值