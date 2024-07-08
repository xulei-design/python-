# 魔法方法，也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1.不需要手动调用，会在合适的时机自动调用
# 2.这些方法都是使用 __ 开始，使用 __ 结束
# 3.方法名都是系统规定好的，在合适的时机自己调用


class Person(object):
    # 在创建对象时，会自动调用这个方法
    def __init__(self, name, age):
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):  # 当程序结束时会自动调用
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名:{},年龄：{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print('__call__方法被调用了')
        # *args保存的是一个元组，保存(1,2)
        # **kwargs 保存的是一个字典{fn:lambda x ,y:x+y}
        print('args={},kwargs={}'.format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


x = Person('张三', 18)
# print(x) # 如果不做任何的修改，直接打印一个对象，是文件的 __name__.类型  内存地址
# <__main__.Person object at 0x000001FCEB78E208>

# 当打印一个对象的时候，会调用对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都写了，选择 __str__
print(x)

# 把一个对象当作函数来调用
n = x(1, 2, fn=lambda x, y: x + y)  # 对象名() ==> 调用这个对象的 x.__call__(1,2)方法
print(n)

# time.sleep(10)


# print(repr({'name':'zhangsan','age':18})) # {'name': 'zhangsan', 'age': 18}

# print(repr(x)) # 调用内置函数 repr 会触发对象的 __repr__ 方法
# print(x.__repr__()) # 魔法方法，一般不手动调用


# 当创建一个对象时，会自动调用__init__方法，当删除一个对象时，会自动调用__del__方法。
# 使用__str__和__repr__方法，都会修改一个对象转换成为字符串的结果。
# 一般来说，__str__方法的结果更加在意可读性，而__repr__方法的结果更加在意正确性(例如:datetime模块里的datetime类)


import datetime

y = datetime.datetime(2020, 3, 8, 13, 41, 20)
print(y)  # 调用的是 __str__ 方法
print(repr(y))  # __repr__ 方法
