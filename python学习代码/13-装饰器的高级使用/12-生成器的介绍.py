# 生成器其实就是一种迭代器，是一种比较特殊的迭代器
# 迭代器是一个对象，生成器是一个函数

# 最简单的生成器
x = [i for i in range(10)] # 列表推导式：x是一个列表

y = (i for i in range(10)) # 生成器，其实就是迭代器
print(type(y))  # y是一个生成器类型

print(next(y)) # 既然是迭代器，就能够手动调用next方法
for x in y:
    print(x)