# 列表可以使用extend方法将两个列表合并成为一个列表
nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]
nums1.extend(nums2)
print(nums1)

# 使用update将两个字典合并成一个
person1 = {'name': 'xulei', 'age': 18}
person2 = {'addr': '襄阳', 'height': 180}
person1.update(person2)
print(person1)

# 元组的合并，不改变原有的元组，而是得到了一个新的结果
word1 = (1, 2, 3, 4)
word2 = (5, 6, 7)
print(word1 + word2)

# 字典不能做加法运算
# print(person1 + person2)