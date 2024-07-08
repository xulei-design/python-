class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我么称之为类属性，类属性，保存在类对象里

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象P1和p2是通过Person类创建出来的实例对象
# name和age是对象属性，在__init__方法里，以参数的形式定义的
# 每一个实例对象都会单独保存一份的属性
# 每个实例对象之间没有关联，互不影响
p1 = Person('张三', 18)
p2 = Person('李四', 19)

# p1.name = '许磊'
# x = p1
# print(p1.name)
# print(x.name)

# 类属性得以通过类对象和实例对象获取
print(Person.type)  # 可以的通过类对象获取类属性

# 也可以通过实例对象来获取类属性
print(p1.type)
print(p2.type)

# 类属性只能通过类对象来修改，实例对象无法修改
# p1.type = 'xulei'  # 给实例对象添加了一个type实例属性，而不是改变类属性里的type值
# print(p1.type)  # xulei
# print(p2.type)  # 人类
# print(Person.type)  # 人类

# 类对象的修改
Person.type = '王五'
Person.math = 80
print(p2.type)  # 王五
print(p1.type)  # 王五
Person.math = 98
print(Person.__dict__)
