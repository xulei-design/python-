# 正则表达式作用是对字符串进行检索和替换
# 检索： match search findall fullmatch  finditer
# 替换：sub
import re

t = 'afonheb29hb72bq90iib13095'
print(re.sub(r'\d', 'x', t))  # afonhebxxhbxxbqxxiibxxxxx
print(re.sub(r'\d+', 'x', t))  # afonhebxhbxbq]xiibx  把多个数字变成了一个

p = 'hello39good23'  # 把字符串里的数字*2 hello68good46


# 第一个参数：正则表达式
# 第二个参数：新字符或者函数
# 第三个参数：需要被替换的原来的字符串
def test(n):
    y = int(n.group(0))
    y *= 2
    return str(y)


# sub内部再调用test方法时，会把每一个匹配到的数据以 re.Match 的格式传参
print(re.sub(r'\d+', test, p))  # test 函数是自动调用
