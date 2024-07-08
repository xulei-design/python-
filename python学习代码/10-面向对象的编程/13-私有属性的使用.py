import datetime


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的属性是私有属性

    # def test(self):
    #     self.__money += 10  # 可以在这里访问私有属性

    def get__money(self):
        # 记录
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    # 私有变量的更改
    def set_money(self, qian):
        if type(qian) != int:
            print('设置的余额不合法')
            return
        print('修改了余额')
        self.__money = qian

    def __test(self): # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是__test函数，我被调用了')


p = Person('zhangsan', 18)

p.set_money(2000)
print(p.age, p.name)  # 可以直接获取
# print(p.__money) # 不能够直接获取私有变量

# p.test()

# 获取私有变量的方式
# 1. 使用 对象._类名__私有变量名  获取
# print(p._Person.__money)  # 这种方式也能够获取到私有变量
# 2. 定义get和set方法来获取
print(p.get__money())

# 3. 使用property来获取()
