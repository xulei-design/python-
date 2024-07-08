class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =cuisine_type

    def describe_restaurant(self):
        print('这个饭店的名字是'+self.restaurant_name.title()+'.')
        print('所做的菜系是'+self.cuisine_type.title()+'.')

    def open_restaurant(self):
        print(self.restaurant_name,'正在营业')

rst1 = Restaurant('光影餐厅', 'Chinese cuisine')

# 1.实例对象访问属性
print(rst1.restaurant_name)
print(rst1.cuisine_type)
# 2.实例对象调用方法
rst1.describe_restaurant()
rst1.open_restaurant()

# 创建多个对象
print('-----------------------------------')
rst1.describe_restaurant()
rst2 = Restaurant('米其林餐厅','western food')
rst3 = Restaurant('重庆火锅','sicuan cuisine')
rst2.describe_restaurant()
rst3.describe_restaurant()
print('----------------------------------------------')

