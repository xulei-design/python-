class Person(object):
    __slots__ = ('name', 'age')
    '''
    这是一个人类
    '''

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def eat(self):
        print(self.name, '正在吃饭')


p = Person('zhangsan', 19)
# 所有的属性和行为都列出来
print(dir(p))
print(p.__class__)  # <class '__main__.Person'>
# print(p.__dict__)  # {'age': 19, 'name': 'zhangsan'} 把对象属性和值转换成一个字典
# print(p.__dir__()) # 等价于print(dir(p))
print(p.__doc__)  # 对类的多行注释的说明 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__

print(p.__module__)  # __main__
