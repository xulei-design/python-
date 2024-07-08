# 有一个列表 names，保存了一组姓名 names = ['zhangsan','lisi','chris','jerry','herry']
# 在让用户输入一个姓名，如果这个姓名在列表里存在，提示用户名已存在
# 如果这个姓名在列表里不存在，将这个姓名添加到列表里

# names = ['zhangsan', 'lisi', 'chris', 'jerry', 'herry']
# name = input('请再输入一个姓名：')

# 法一 （遍历法）
# for x in names:
#     if x == name:
#         print('用户名已存在')
#         break
# else:
#     names.insert(0, name)
#     print(names)

# 法二 （计数法）
# if names.count(name) == 0:
#     names.append(name)
#     print(names)
# else:
#     print('用户名已存在')

# 法三 （if...in...语句判断法）
# if name in names:
#     print('用户名已存在')
# else:
#     names.append(name)
#     print(names)

# 统计列表里出现次数最多的元素
# 冒泡完善
# 求列表里的最大数
# 删除列表里的空字符串

