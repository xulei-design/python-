# 冒泡排序思想：
# 让一个数字和他相邻的下一个数字进行比较运算
# 如果前一个数大于后一个数字，交换两个数据的位置

# nums[0]  nums[1]
# nums[1]  nums[2]
# ... ...
# nums[n]  nums[n+1]
# ... ...
# nums[length-2]  nums[length-1]

# 每一趟比较次数的优化
# 总比较趟数的优化
nums = [6, 5, 3, 1, 8, 7, 2, 4]  # 长度是8
count = 0
i = 0
while i < len(nums) - 1:
    i += 1
    n = 0
    while n < len(nums) - 1:
        # print(nums[n], nums[n + 1])
        count += 1
        if nums[n] > nums[n + 1]:
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n += 1
print(nums)
print('比较了%d次' % count)


# 冒泡排序的优化(假设法）
nums = [6, 5, 3, 1, 8, 7, 2, 4]  # 长度是8
count = 0
i = 0
# 第一趟比较时，i=0，多比较了0次
# 第二趟比较时，i=1，多比较了1次
# 第三趟比较时，i=2，多比较了2次

while i < len(nums) - 1:
    # 在每一趟都定义一个flag
    Flag = True # 同时更改所有变量名：点击所要修改的变量名，右键-->Refactor--->rename
    n = 0
    while n < len(nums) - 1 - i:
        # print(nums[n], nums[n + 1])
        count += 1
        if nums[n] > nums[n + 1]:
            # 只要交换了，假设就不成立
            Flag = False
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n += 1
    if Flag:
        # 这一趟走完以后，flag依然是 True,这说明这一趟没有进行过数据交换
        break
    i += 1
print(nums)
print('比较了%d次' % count)