# 手动指定Person类继承自object
class Person(object): # 兼容性问题
    pass

#没有指定Dog的父类，python3里默认继承自object
class Student:
    pass

# 新式类和经典类的概念
# 1. 新式类：继承自Object 的类我们称之为新式类
# 2. 经典类：不继承object 的类

# 在python2里，如果不手动的指定一个类的父类时object，这个类就是一个经典类
# 在python3里不存在经典类，都是新式类