class A(object):
    def demo_a(self):
        print('我是A类里的demo_a方法')

    def foo(self):
        print('我是A类里的foo方法')

class B(object):
    def demo_b(self):
        print('我是B类里的demo_b方法')

    def foo(self):
        print('我是B类里的foo方法')


# python里允许多继承
class C(A,B): # 如果不写父类，python3以后，默认自动继承object
    pass

c = C()
c.demo_a()
c.demo_b()

# 如果两个不同的父类有同名方法（先到先得），有一个类属性可以查看方法的调用顺序
c.foo()
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)