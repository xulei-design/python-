print('hello'.rindex('h'))  # 结果是 0

# 修改大小写（只适用于英文）

# capitalize 让第一个单词的首字母大写
print('hello world\nyes'.capitalize())

# upper 全部大写
print('hello'.upper())

# lower 全小写
print('EddiTION'.lower())  # 面向对象里，称之为方法

# title 每个单词的首字母大写
print('good morning'.title())

# 不区分大小写
# while True:
#     content = input('请输入内容，输入exit退出')
#     print('你输入的内容是', content)
#
#     if content.lower() == 'exit':
#         break


# ljust(length)
# width 长度  fillchar 填充字符，默认空格
# 让字符串以指定的长度显示，如果长度不够，默认在右边使用空格补齐或者指定的字符补齐。
print('Monday'.ljust(12, '='))
print('Tuesday'.rjust(12, '+'))
print('apple'.center(20, '*'))


#去除空格 strip
print('++++apple++++'.lstrip('+')) # 去除左边空格
print('    apple    '.rstrip()) # 去除右边空格
print('   apple   '.strip())  # 去除所有空格


# 以某种固定格式显示的字符串，我们可以将它切割成一个列表
x = 'zhangsan+lisi+wangwu+jack+tony'
names=x.split('+')
print(x.split('+'))
print(names)

# 将列表转换成字符串
fruits=['apple','pear','peach','banana','orange']
print('-'.join(fruits))
print('*'.join('hello')) # iterable  可迭代对象

# 字符串之间的运算符
# 字符串和字符串之间可以使用加法运算，作用是拼接两个字符串
# 字符串和数字之间可以做乘法运算，目的是将指定的字符串重复多次
# 字符串和数字之间做 == 运算结果是Flase, 做 ！= 运算结果是True
# 字符串与字符串之间可以做比较运算，会逐个比较字符串的 ASCII 编码值
# 不支持其他运算符