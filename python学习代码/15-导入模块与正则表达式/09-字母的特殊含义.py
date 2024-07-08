import re
# 字母表示他本身，很多字母前面加 \ 会有特殊含义

# \n 换行    \t: 表示一个制表符   \s:空白字符     \S:非空白字符
# \d:表示数字，等价于[0-9]
print(re.search(r'x\d+p', 'x525p'))
print(re.search(r'x[0-9]+p', 'x525p'))

# \D 表示非数字
# v = re.search(r'\D+','he11o')
v = re.search(r'[^0-9]+','he11o')
print(v)

# \w:表示数字，字母,中文以及 _ 等价于 [0-9a-zA-Z_] 非标点符号
print(re.search(r'\w+', 'hE+110_*.-'))
print(re.findall(r'\w+', 'hE+110_*.-'))

# \W: \w取反 （标点符号）
print(re.findall(r'\W+', 'hE+110_*.-'))