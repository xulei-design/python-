# 去重排序
nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
# 去重，将列表转换为集合即可去重，因为集合中的元素时不重复且无序的
x = list(set(nums))
x.sort(reverse=True)
print(x)
