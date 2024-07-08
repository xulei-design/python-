# 查找相关的方法
# match:查找字符串，返回的结果是一个re.Match对象
# search:查找字符串，返回的结果是一个re.Match对象
# finditer:查找到所有的匹配数据，放到一个可迭代对象里
# findall:把查找到的所有的字符串结果放到一个列表里
# fullmatch:完整匹配，字符串需要满足完整正则规则才会有结果，否则就是None    

import re

# match 和 search
# 共同点：1.只对字符串查询一次  2.返回值类型都是 re.Match类型对象
# 不同点：match 是从头开始匹配（开头匹配），一旦匹配失败，就返回None;search是在整个字符串里匹配
from collections.abc import Iterable

m1 = re.match(r'hello', 'hello world good morning')
print(m1)  # <re.Match object; span=(0, 5), match='hello'> (0,5)左开右闭

m3 = re.match(r'good', 'hello world good morning')
print(m3)  # None
m2 = re.search(r'good', 'hello world good morning good')
print(m2)  # <re.Match object; span=(0, 5), match='hello'>

# print(re.search(r'x', 'kxdioaebgxbxjbsx')) 只会查找一个'x'

# finditer 返回的结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果，是一个 re.Match 类型的对象
z = re.finditer(r'x', 'kxdioaebgxbxjbsx')
print(z)
print(isinstance(z, Iterable)) # 查看返回结果z是否是可迭代对象

for t in z:
    print(t)

n = re.findall(r'x\d+', 'kx45dioaebgxbx5jbsx')
print(n)

m = re.fullmatch(r'helloworld','helloworld')
print(m)

m6 = re.fullmatch(r'h.*d','hedhzdazdhrld') # 以h开头，d 结尾
print(m6)