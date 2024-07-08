import re

# \s 表示任意的非打印字符 以下都是非打印字符  （空白字符）
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\n', 'hello\nworld'))  # 换行
print(re.search(r'\s', 'hello\tworld'))  # 制表符

# \S 表示非空白字符
print(re.search(r'\S', '\t\n   x'))

# 标点符号的使用
# (): 用来表示一个分组
m = re.search(r'h(\d+)x', 'sh829xkfl4sa')
print(m.group(1))

# 如果要表示括号，要使用 \
m1 = re.search(r'\(.*\)', '(1+1)*3+5')
print(m1.group())

# . 匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。

# []用来表示可选项范围 [x-y]表示从x到y区间，包含x和y
# m2 = re.search(r'f[0-5]m', 'pdsf0m')
# m2 = re.search(r'f[a-c]m', 'pdsfbm')
# m2 = re.search(r'f[0-5]+m', 'pdsf1245m') # 加号表示出现一次或者多次
m2 = re.search(r'f[0-5,a-d]m', 'pdsfcm')  # 区间内表示或者的关系 0<=value<=5 或则 a<=value<=d
print(m2)

# | 用来表示或者 和 []有一定的相似，但有区别
# [] 里的值表示区间，而且是单个字符
# | 就是可选值，可以出现多个值
m3 = re.search(r'f(x|prz|t)m', 'pdsfprzm')
print(m3)

# {} 用来限定前面元素出现的次数
# {n}:表示前面的元素出现 n 次
# {n,}:表示前面的元素出现 n 次及其以上
# {,n}:表示前面的元素出现 n 次及其以下
# {m,n}:表示前面的元素出现 m 到 n 次
# m4 = re.search(r'go{2}d', 'good')
# m4 = re.search(r'go{2,}d', 'goooood')
# m4 = re.search(r'go{,2}d', 'god')
m4 = re.search(r'go{1,2}d', 'good')
print(m4)

# *: 表示前面的元素出现任意次数(0次及以上) 等价于 {0,}
print(re.search(r'go*d', 'goooood'))
# +:表示前面的元素至少出现一次，等价于 {1,}
print(re.search(r'go+d', 'gooood'))

# ?:两种用法：
# 1.规定前面的元素最多只能出现一次，等价于 {,1}
# 2.将贪婪模式转换为非贪婪模式
print(re.search(r'go?d', 'god'))

# ^ 以指定的内容开头，在[]中还可以表示取反    $: 已制定内容结尾
n = re.search(r'^a.*i$', 'afuahguhsi')
print(n)
