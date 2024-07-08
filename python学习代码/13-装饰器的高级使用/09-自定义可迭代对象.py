# 可迭代对象并不是继承自 Iterable 类，而是重写了 __iter__方法
import time
from collections.abc import Iterable
from collections.abc import Iterator


class MyIterable(object):
    def __init__(self, count):
        self.count = count
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n +=1
        if self.n <= self.count:
            return 'hello'
        else:
            raise StopIteration # 迭代器停止

class Person(object):
    def __init__(self, name):
        self.name = name

    def __iter__(self):  # 只要一个类重写了__iter__方法，他就是可迭代对象
        # 必须要返回一个迭代器，for...in循环时，会获取到这个返回值对象，调用它的 __next__方法
        myIt = MyIterable(10)
        print('myIt是否是迭代器{}'.format(isinstance(myIt, Iterator)))
        return myIt


p = Person('明明')
print(isinstance(p, Iterable))

# 如果一个对象重写了__iter__方法，它就是一个可迭代对象
# 可迭代对象可以使用for...in循环进行遍历
# iter() returned non-iterator of type 'NoneType'
# iter方法返回的结果是空(NoneType)，它是一个非iterator(迭代器)
#
# __iter__方法到底做了什么工作呢？
# 判断一个对象是否是迭代器？
# 一个对象要想变成迭代器，需要重写__iter__方法和__next__方法
print(isinstance(p, Iterator))

# for...in循环的本质是，获取到的迭代对象的迭代器，然后不断地调用迭代器的 next 方法
# __iter__返回值必须是一个迭代器
# for x in p:
#     print(x)
print(p.__iter__().__next__())

# next 和 iter
print(next(iter(p)))
i = iter(p) # 获取到迭代器
next(i) # 调用迭代器中的Next方法
