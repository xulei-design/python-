# signature 签名
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print('__eq__方法被调用了', other)
        if self.name == other.name and self.age == other.age:
            return True
        return False


# 1.调用 __new__ 方法申请内存空间，p1和p2申请的内存空间不同，所以是不同的对象
p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

# p1 和 p2是同一个对象吗？ 不是
# 怎样比较两个对象是否是同一个对象呢？ 通过比较内存地址
print('0x%X' % id(p1))  # 0x1AED3B9E148
print('0x%X' % id(p2))  # 0x1AED3B9E188

# is 身份运算符 可以判断是否是同一个对象
print(p1 is p2)  # False

# __eq__ 如果不重写，默认比较仍是内存地址
print(p1 == p2)  # False  p1==p2本质是调用 p1.__eq__(p2),获取这个方法的返回结果

# is 比较两个两个对象的内存地址
# == 会调用对象的 __eq__ 方法，获取这个方法的比较结果
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(nums1 is nums2)  # False
print(nums1 == nums2)  # True
print('nums1的地址是0x%X' % id(nums1))
print('nums2的地址是0x%X' % id(nums2))
