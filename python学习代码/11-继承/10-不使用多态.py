
class PolicDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class Bland_Dog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class Drug_Dog(object):
    def search_drug(self):
        print('缉毒犬正在搜寻毒品')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_pd(self):
        print(self.name + '正在工作')
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.lead_road()

    def work_with_dd(self):
        self.dog.search_drug()


# pd = PolicDog()
p = Person('张三')

pd = PolicDog()
p.dog = pd
p.dog.attack_enemy()

bd = Bland_Dog()
p.dog = bd
p.work_with_bd()

dd = Drug_Dog()
p.dog = dd
p.work_with_dd()

# 此代码的变量是狗的种类和不同狗种类的不同方法
# 用两个变量替代上面代码中两个变得量