class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'hello'

    def __repr__(self):
        return '姓名{}，年龄{}'.format(self.name, self.age)


p1 = Person('张三', 18)
p2 = Person('lisi', 50)
print(p1)
print([p1, p2])  # 打印一个列表会调用__repr__方法
