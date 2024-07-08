# all里面必须是可迭代对象，
# 如果可迭代对象中，每个元素转换成布尔值都是True，结果是True.可迭代对象中的元素有一个是False，结果就是False
# print(all(['hello', 'good', 'yes']))
#
# print(all(['hello', 0]))

# dir: 列出对象所有的属性和方法
nums = [1, 2, 3]
print(dir(nums))

print(dir('hello'))

# shang, yushu = divmod(15, 2)
#
# # help 又来查看帮助文档
# help(int)