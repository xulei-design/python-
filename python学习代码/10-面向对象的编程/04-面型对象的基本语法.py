# 小明今年18 岁，身高 1.75，每天早上跑完步，会去 吃 东西
# 小美今年17 岁，身高 1.65，小美不跑步，小美喜欢 吃 东西

# 定义类：类名怎么定义？  使用 class 来定义一个类
# class 类名:    类名一般遵守大驼峰命名法，每一个单词的首字母都大写
# 1. class <类名>:
# 2. class <类名>（object):


class Student(object):  # 关注这个类有哪些特征和行为
    # 在 __init__方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')


    def eat(self):
        print('正在吃东西')



# 使用 Student 类创建了两个实例对象 s1 s2
# s1和s2都会有name,age,height（特征）属性，同事都有run 和 eat方法
s1 = Student('小明', 18, 1.75)  # Student()==> 会自动调用 __init__ 方法
s2 = Student('小美', 17, 165)

# 根据业务逻辑，让不同的对象执行不同的行为
s1.run()
s1.eat()
s2.eat()




print('0x%X,0x%X,0x%X,0x%X,0x%X,0x%X'%(id(Student),id(s1),id(s2),id(s1.eat),id(s2.eat),id(s1.run)))