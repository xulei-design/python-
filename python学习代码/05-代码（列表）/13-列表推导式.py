# 列表推导式作用是使用简单的语法创建一个列表

nums = [i for i in range(10)]
print(nums)

# nums =[]
# for i in range(10):
#     nums.append(i)
# print(nums)

x = [i for i in range(10) if i % 2 == 0]
print(x)

# x = []
# for i in range(10):
#     if i % 2 == 0:
#         x.append(i)
# print(x)

# points 是一个列表，列表里的元素是 元组
points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)

# 练习：请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
nums = [i for i in range(1, 101)]
print(nums)
# 使用列表推导式
m = [nums[j:j + 3] for j in range(0, 100, 3)]
print(m)
# m = []
# i = 0
# while i < len(nums):
#     m.append(nums[i:i + 3])
#     i += 1
# print(m)
