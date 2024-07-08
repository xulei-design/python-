nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# nums.sort()
# print(nums[len(nums)-1])

# x = sorted(nums)
# print(x[-1])

# 假设法（假设某个数是最大数）
x = nums[0]  # 假设第0个是最大数
index = 0
# for num in nums:
#     if num > x:  # 如果发现列表里存在比假设还要大的数字
#         # 说明假设不成立
#         num, x = x, num
# print('发现的最大数是%d，最大数的下标%d' % (x, nums.index(x))
i = 0
while i < len(nums):
    if nums[i]>x:
        x = nums[i]
        index = i
    i += 1
print('发现的最大数是%d，最大数的下标%d' % (x, index))
