class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name+'正在吃' + food)

    def sleep(self):
        print('正在睡觉')

p = Person('zhangsan')
# p.eat('西红柿鸡蛋')
eat = p.eat # 给对象的eat方法起了一个别名
