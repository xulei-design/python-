# compile 编译
# 在re模块里，可以使用 re.方法 调用函数，还可以调用 re.compile得到一个对象

import re

# 可以直接调用re.search方法
m = re.search(r'm.*a', 'o3rjomjadas')
print(m)


# 用一个正则规则，匹配多个字符串
r = re.compile(r'm.*a')
x = r.search('o3rjomjadas')
print(x)
