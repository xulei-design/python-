# 删除列表里的空字符串
words = ['hello', 'good', '', '', 'yes', 'ok', '']  # 去除所有的空字符串

# 在使用for...in 循环遍历列表时，最好不要对元素进行增删操作
# for word in words:
#     if word == '':
#         words.remove(word)
# print(words)

# 遍历删除与增加元素，要注意下标问题
# i = 0
# while i < len(words):
#     if words[i] == '':
#         words.pop(i)
#         i -= 1
#     i += 1
# print(words)

# 创建一个新列表
words2 = []
for word in words:
    if word != '':
        words2.append(word)
    words = words2
print(words)
