# 我们学过的可迭代对象的数据类型有哪些
from collections.abc import Iterable

m = 10
a = 'hello'
b = ['婷婷', '明明', '佳佳', '坤坤']
c = ('yes', 'good', 'hello')
d = {1, 2, 3, 5, 9}
person={'name':'zhangsan','age':18}
nums = range(10)

# 如何判定一个对象是否是可迭代对象
print('-'*20)
print(isinstance(b, Iterable))
print(isinstance(m, Iterable))
print(isinstance(a, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(person, Iterable))

