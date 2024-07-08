class Calculator(object):


    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b




# c=Calculator()
# print(c.add(1, 2))
print(Calculator.add(1, 2))
print(Calculator.minus(6, 2))


class Person(object):
    type = 'human'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # eat 方法存储在类属性里，对象方法有一个参数self，指的是实例对象
        print(self.name + '正在吃' + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法定义成static，这种方法叫做静态方法
    @staticmethod
    def demo():  # 注意括号里面什么都不用， 默认的方法都是对象方法
        print('hello')

    @classmethod
    def test(cls):  # 如果这个函数只用到了类属性，我们可以把它定义成为一个类方法
        # 类方法就有一个参数cls，也不需要手动传参，会自动传参
        # cls 指的是类对象  cls is Person==>True
        print(cls.type)
        print('yes')


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

# 实例对象再调用方法时，不需要给形参self传参，会自动把实例对象传递给self
# eat对象方法，可以直接使用 实例对象.方法名(参数) 调用
# 使用 对象名.方法名(参数）调用的方式，不需要传递self
# 会自动将对象名传递给self
p1.eat('红烧牛肉泡面')  # 直接使用实例对象调用方法

# 对象方法还可以使用 类对象来调用 类名.方法名()
# 这种方式，不会自动给self传参，需要手动调用指定的s elf
Person.eat(p2, '西红柿盖饭')

# print(p1.eat)
# print(p2.eat)
# print(Person.eat)


# 因为p1和eat方法绑定和p2和eat 绑定不是同一个对象
# print(p1.eat is p2.eat)  # False


# 静态方法的调用，没有用到实例对象的任何属性
Person.demo()
p1.demo()

# 类方法的调用，类方法可以使用实例对象和类方法来调用
# print(p1.type)
p1.test()
Person.test()