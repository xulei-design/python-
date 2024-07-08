def test(a):
    print('修改前a的内存地址0x%X' % id(a))
    a = 100
    print('修改后a的内存地址0x%X' % id(a))


def demo(nums):
    print('修改前nums的内存地址0x%X' % id(nums))
    nums[0] = 10
    print('修改后nums的内存地址0x%X' % id(nums))


# 可变数据类型，指向同一个位置，不可变数据类型，不同指向
x = 1
test(x)
print(x)  # 1
print('x的地址0x%X' % id(x))

y = [3, 4, 5, 6, 8, 2]
print('修改前y的内存地址0x%X' % id(y))
demo(y)
print('修改后y的内存地址0x%X' % id(y))
print(y)  # [10, 4, 5, 6, 8, 2]
