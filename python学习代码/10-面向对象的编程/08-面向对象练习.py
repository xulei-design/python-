# 房子有户型，总面积，剩余面积(等于总面积的%60），和家具名称列表属性
# 新房子里没有任何的家具
# 判断家具的面积是否超过剩余面积，如果超过，提示不能添加家具
# 将家具的名称追加到家具名称列表中

# 家具（furniture)有名字和占地面积属性，其中
# 席梦思（bed）占地4平米
# 衣柜（chest) 占地2平米
# 餐桌（table) 占地1.5平米
# 将以上三件家具添加到房子里
# 打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表
# default 违约，缺省

class House(object):
    # 缺省参数
    def __init__(self, house_type, total_area, fur_list=None):
        if fur_list is None:  # 如果这个只是None
            fur_list = []  # 将fur_list设置为空列表

        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fur_list = fur_list

    def add_fur(self, x):  # x = bed
        if self.free_area < x.area:
            print('剩余面积不足，不能添加家具')
        else:
            self.fur_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return '户型={},总面积={}，剩余面积={},家具列表={}'.format(self.house_type,self.total_area,self.free_area,self.fur_list)



class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传入户型和总面积
house1 = House('以室一厅', 20 )

sofe = Furniture('沙发',10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 把家具添加到房间里(面向对象的关注点：让谁做）
house1.add_fur(sofe)
house1.add_fur(bed)
house1.add_fur(chest)
house1.add_fur(table)

# print(house1.__str__)
print(house1)  # print打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取他们的返回值

