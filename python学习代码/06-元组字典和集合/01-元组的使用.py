# 元组和列表很像，都是用来保存多个数据
# 使用一对（ ）来表示一个元组
# 元组和列表的区别在于列表是可变的，而元组是不可变数据类型,元组不能直接修改
words = ['hello', 'yes', 'good', 'hi']  # 列表，使用 [] 表示
nums = (9, 6, 3, 1, 4, 7, 6)  # 元组，使用 ( )来表示

# 和列表一样，也是一个有序的存储数据的容器
# 可以通过下标来获取元素
print(nums[3])

# 查询元组 index  count
x = nums.index(9)
print(x)
print(nums.count(6))

# 特殊情况：如何表示只有一个元素的元组？
# ages = (18)  # 这种书写方式，ages 是一个整数，并不是一个元组
ages = (18,)  # 如果元组里只有一个元素，要在后面加，
print(type(ages))

# tuple 内置类
# print(tuple(18))
print(tuple('hello')) # ('h', 'e', 'l', 'l', 'o')
# 跟可迭代对象


# 怎么样将列表转换元组？ 将元组转换成列表？
print(tuple(words))  # tuple list set 都是这样使用
print(list(nums))  # 将元组转换成列表

height=('186','174','180')
print('*'.join(height))
print(''.join(('h', 'e', 'l', 'l', 'o')))

# 元组也可以遍历
for i in nums:
    print(i)