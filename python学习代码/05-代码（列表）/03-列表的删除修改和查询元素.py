master = ['王昭君', '小乔', '沈梦溪', '武则天', '妲己', '貂蝉']

# 删除数据的三个方法： pop  remove  clear
# pop 方法默认会删除列表里的最后一个数据，并且返回这个数据
# Pop 还可以传入index 参数，用来删除指定位置上的数据
x = master.pop(3)
print(x)  # 武则天
print(master)  # ['王昭君', '小乔', '沈梦溪', '妲己', '貂蝉']

# remove 用来删除指定的元素
master.remove('小乔')
# master.remove('武则天') # 删除的元素数据不存在，会报错
print(master)

# 使用del 也可以删除一个数据（少用）
del master[2]
print(master)

# clear 用来清空一个列表
master.clear()
print(master)

tanks = ['亚瑟', '程咬金', '盾山', '牛魔王', '廉颇', '程咬金']

# 查询相关的方法 index count
print(tanks.index('盾山'))  # 2
# print(tanks.index('庄周')) 如果元素不存在会报错
print(tanks.count('程咬金'))  # 2
# in 运算符
print('张飞' not in tanks)  # True
print('张飞' in tanks)  # False

# 修改元素
# 可以使用下标直接修改列表里的元素
tanks[5] = '庄周'
print(tanks)
