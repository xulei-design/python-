# 调用re.match , re.search或则对 re.finditer 结果进行遍历
# 拿到的内容都是 re.Match类型对象

import re

# .任意字符  * 出现任意次数  贪婪模式和非贪婪模式
m = re.search(r'm.*a','ajagb3mfhaiha')# <re.Match object; span=(6, 7), match='m'>
# print(m.__dir__()) # 查看re.Match类型对象的所有属性
# print(m.pos,m.endpos)
print(m.span()) # 匹配到的结果字符串的开始下标，还能够拿到指定分组的开始字符串的下标

# 使用group方法可以获取匹配的字符串结果
# group 可以传参，表示第 n 个分组
print(m.group()) # mfhaiha
print(m.group(0))# mfhaiha
# print(m.group(1)) # IndexError: no such group

# group 方法表示正则表达式的分组
# 1.在正则表达式里使用 ( )表示一个分组
# 2.如果没有分组，默认只有一组
# 3.分组的下标从 0 开始

# 正则表达式有 四个 分组
m1 = re.search(r'(9.*)(0.*)(5.*7)','agpa9wkbi0uagbio5abf7ba')
print(m1.group(0)) # 第0组就是把整个正则表达式当作一个整体，默认就是第0组
print(m1.group(1)) # 9wkbi
print(m1.group(2)) # 0uagbio
print('-'*1000)
print(m1.groups())
# 分组0：(9.*)(0.*)(5.*7)
# 分组1：(9.*)

# groups 拿到分组匹配数据，存放到元组中
print(m1.groups()) # ('9wkbi', '0uagbio', '5abf7')

# groupdict 作用是获取到分组组成的字典
print(m1.groupdict()) # {}

# (?p<name>表达式) 可以给分组起一个名字
m2 = re.search(r'(9.*)(?P<xxx>0.*)(5.*7)','agpa9wkbi0uagbio5abf7ba')
print(m2.groupdict())
print(m2.groupdict('xxx')) # 获取到的是一个字典 {'xxx': '0uagbio'}

# group可以通过分组名或则分组的下标获取到分组里匹配到的字符串