class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


p1 = Person('张三', 18)
p2 = Person('张三', 18)
s = Student('jack', 20)

# 获取两个对象的内存地址 id(p1) == id(p2)
# print(p1 is p2)  # is身份运算符是用来比较是不是同一个对象

# type(p1) 其实获取的就是类对象
# a = 1
# if type(a) == int:
#     print('a是一个整数类型')
#
# if type(p1) == Person:
#     print('p1是Person类创建出来的实例对象')
#
# # s 这个实例对象是否是由Students创建的
# print(type(s) == Student)
# print(type(s) == Person)

# isinstance 用来判断一个对象是否是由指定的对象（或者父类）实例化出来的
print(isinstance(s, Student))
print(isinstance(s, Person))

print(isinstance(p1, Person))
print(isinstance(p1, Student))

# issubclass 用来判断一个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))
