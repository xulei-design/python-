class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        # print('__setitem__被调用了，key={},value={}'.format(key, value))
        # __setitem__被调用了，key=name,value=lisi
        p.__dict__[key] = value

    def __getitem__(self, item):
        return p.__dict__[item]


p = Person('zhangsan', 18)
print(p.__dict__)  # 将对象转换成为一个字典 {'name': 'zhangsan', 'age': 18}

# 不能把对象直接当作一个字典来使用
p['name'] = 'lisi'  # []语法会调用对象的 __setitem__ 方法
print(p.name, p.age)
p['age'] = 20
print(p.name, p.age)
p.age = 85
print(p.name, p.age)

print(p['name'])  # 会调用 __getitem__ 方法
