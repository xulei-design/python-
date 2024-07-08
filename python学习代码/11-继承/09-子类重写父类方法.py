# 继承特点：如果一个类A继承自类B，由类A创建出来的实例对象都能够使用类B里的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


# p = object.__new__(Person)
# # p.__init__('zhangsan', 18)
# Person.__init__(p, 'zhangsan', 18)


class Student(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        # 子类在父类实现的基础上，有添加新的功能
        # 调用父类的两种方法（属性）（子类在父类的基础上又有更多的实现，在子类的基础上先调用一下父类）
        # 1. 父类名.方法名(self,参数列表)
        # Person.__init__(self, name, age) # 此时的self相当于实例对象s
        # 2.使用super直接调用父类的方法。推荐使用第二种方式
        super(Student, self).__init__(name, age)
        self.school = school

    def sleep(self):
        print(self.name + '正在课间休息室睡觉')

    def study(self):
        print(self.name + '正在学习')


s = Student('jerry', 20)  # 调用了父类的 __init__方法
s.sleep()  # 调用了父类的
print(Student.__mro__)  # 方法调用的顺序

# 1.子类的实现和父类的实现完全不一样，子类可以选择重写父类的方法
# 2.子类在父类的基础上又有更多的实现
