class Animal(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def eat(self):
        print(self.name + "正在吃东西")

    def __test(self):
        print('我是Animal类里的__test方法')


class Person(Animal):
    def __demo(self):
        print('我是Person类里的私有方法__demo')


p = Person('张三', 19, 500)
print(p.name)
p.eat()
Person.eat(p)
p._Person__demo()  # 自己类里定义的私有方法  对象名._类名__私有方法()
p._Animal__test()  # 可以通过 对象名._类名__私有方法


# 私有属性和私有方法子类不会继承
# p._Person__test() # 父类的私有方法，子类没有继承

# print(p._Person__money)
print(p._Animal__money)
