class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type, number_severd=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_severd = number_severd

    def describe_rastaurant(self):
        print('餐馆名字是{},餐馆类型是{}餐馆'.format(self.restaurant_name, self.cuisine_type))

    def open_restaurant_name(self):
        print(self.restaurant_name + '餐馆正在营业')

    def set_number_served(self, number_severd):
        self.number_severd = number_severd
        print('有' + str(self.number_severd) + '人就餐')

    def increment_number_served(self, number):
        self.number_severd += number
        print('这家餐馆每天接待的就餐人数是' + str(self.number_severd))


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_severd=0, flavors=None):
        if flavors is None:
            self.flavors = []
        self.flavors = flavors
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type, number_severd)

    def kouwei(self):
        for i in self.flavors:
            print('冰淇凌有' + i + '口味')


i = IceCreamStand('爽爽冰淇凌店', '冷饮',  flavors=['草莓味', '麦香', '可乐'])
i.describe_rastaurant()
i.open_restaurant_name()
i.kouwei()
