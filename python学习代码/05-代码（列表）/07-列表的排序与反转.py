nums = [6, 5, 8, 7, 3, 1, 2, 4]
# 可以调用列表的 sort 方法可以直接对列表进行排序
# 直接对原有的列表进行排序

nums.sort()
print(nums)


# 内置函数 sorted，不会改变原有的列表数据，会生成一个新的有序数据
x = sorted(nums)  # 内置函数 sorted
print(nums)
print(x)


names = ['zhangsan','lisi','wangwu']
names.reverse()
print(names)

print(names[::-1])