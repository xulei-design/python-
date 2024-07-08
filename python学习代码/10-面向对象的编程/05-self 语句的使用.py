class Student(object):
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    __slots__ = ('name', 'age', 'city')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


# Student('张三',18) 这段代码具体做了什么呢？
# 1.调用 __new__ 方法,用来申请内存空间
# 2.调用 __init__ 方法传入(特征）参数，将self 指向创建好的内存空间，填充数据
# 3.变量s1也指向创建好的内存空间
s1 = Student('张三', 18)

print('s1的内存地址是0x%X' % id(s1))
print(s1.name)

# Attribute 属性
# 没有属性，会报错
# print(s1.height)


# 如果直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 如果这个属性以前存在，会修改这个属性
# 动态属性
s1.city = '上海'
print(s1.city)
