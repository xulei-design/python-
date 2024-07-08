# 用来处理字符串，对字符串进行检索和替换
# 1.查找  2.替换
# 看身份证的格式是否正确

import re

x = 'hello\\nworld'
# 在正则表达式里，如果想要匹配一个 \ 需要使用 \\\\

# 第一个参数是正则匹配规则
# 第二个参数表示需要匹配的字符串
# m = re.match('\\\\', x)  # match:匹配
# m = re.search('\\\\', x)

# 还可以在字符串前面加 r,\\就表示 \
m = re.search(r'\\', x)

# search 和 match 方法的执行结果是一个Match类型的对象
print(m) # <re.Match object; span=(5, 6), match='\\'>
