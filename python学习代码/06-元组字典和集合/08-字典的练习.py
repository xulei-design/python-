chars = ['a', 'c', 'b', 'x', 'd', 'p', 'm', 'q', 's', 't', 'a', 't', 'c', 'a', 'c']
# 计算每一个字符出现的次数 {'a':3,'c':2,'b':1,'d':1}
char_count = {}
# for char in chars:
#     if char in char_count:
#         # print('字典里已经有了这个字符%s' % char)
#         pass
#     else:
#         # print('字典里没有这个字符%s' % char)
#         char_count[char] = chars.count(char)
#         # print(char_count)
# print(char_count)

for char in chars:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# 拿取字典里的最大个数的键值对
vs = char_count.values()
# 取最大数可以使用内置函数max 取得最大数
print(max(vs))
max_count = max(vs)
print(char_count.items())
for k, v in char_count.items():
    if v == max_count:
        print(k)
print(type(char_count.items()))
