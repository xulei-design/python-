import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp, radius):
        self.cp = cp
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        print('圆的面积时' + str(area))

    def circle_round(self):
        round = math.pi * self.radius * 2
        print('圆的周长为' + str(round))

    def relationship(self, point):
        '''求一个点和圆的关系。有三种关系：在圆内，在圆上，在园外'''
        R = (self.cp.x - point.x) ** 2 + (self.cp.y - point.y) ** 2
        if R < self.radius ** 2:
            print('点在圆内')
        elif R > self.radius ** 2:
            print('点在圆外')
        else:
            print('点在圆上')


# def judge(self):
#     R = ((self.cp.x - self.x) ** 2 + (self.cp.y - self.y) ** 2) ** (-0.5)
#     if R < self.radius:
#         print('点在圆内')
#     elif R == self.radius:
#         print('点在圆上')
#     else:
#         print('点在圆外')
p1 = Pointer(10, 10)
p = Pointer(3, 4)
c = Circle(p, 5)
c.area()
c.circle_round()
c.relationship(p1)
print('------------------------------------------------------------------------')


class PetShop(object):
    def __init__(self, shop_name):
        # if pet_list is None:
        #     pet_list = []

        self.shop_name = shop_name
        self.pet_list = []

    def add_pet(self, pet):
        self.pet_list.append(pet)
        return self.pet_list

    def get_pet_information(self):
        print('这家宠物点叫' + self.shop_name)
        print('这家店的宠物有' + str(self.pet_list))


class PetDog(object):
    def __init__(self, name, sex, age, type):
        self.name = name
        self.sex = sex
        self.age = age
        self.type = type

    def eat(self):
        print(self.name + '正在吃骨头')

    def cry(self):
        print(self.name + '正在汪汪的叫')

    def pull_down(self):
        print(self.name + '正在拆家')


class PetCat(PetDog):
    def __init__(self, name, age, type, eyes_color):
        super(PetCat, self).__init__(name, age, type, eyes_color)
        self.eyes_color = eyes_color

    def eat(self):
        print(self.name + '正在吃鱼')

    def cry(self):
        print(self.name + '正在喵喵的叫')

    def coquetry(self):
        print(self.name + '正在撒娇')


c = PetCat('托尼', 2, '英短', '蓝色')
c1 = PetCat('托尼', 3, '英短', '蓝色')
c.eat()
c.coquetry()
c.cry()
d = PetDog('哈尼', '公', 3, '法斗')
d1 = PetDog('哈尼', '公', 3, '法斗')
d.eat()
d.cry()
d.pull_down()
