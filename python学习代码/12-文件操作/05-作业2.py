# 建议一个汽车类 Auto
# 包括轮胎个数，汽车颜色，车身重量，速度等属性，斌通过不同的构造方法创建实例
# 至少要求汽车能够加速，减速，停车
# 再定义一个小汽车类CarAuto 继承Auto 并添加空调，CD属性
# 并且重新实现方法覆盖加速，减速方法
class Auto(object):
    def __init__(self, tyre_number, car_color, car_weight,car_speed, *args,  **kwargs):
        self.tyre_number = tyre_number
        self.car_color = car_color
        self.car_weight = car_weight
        self.car_speed = car_speed

    def add_speed(self, add_speed):
        self.car_speed += add_speed
        print('经过加速后的汽车速度是' ,self.car_speed)

    def speed_cut(self, slow):
        self.car_speed -= slow
        print('经过减速后的汽车速度是', self.car_speed)

    def park(self, stop):
        self.car_speed = stop
        if self.car_speed == 0:
            print('车停止了')


car = Auto(4, '黑色', 1.6, 80)
car.add_speed(20)


class CarAuto(Auto):

    def __init__(self, air_condition, cd):
        super(CarAuto,self).__init__(car_color,car_weight,car_speed,tyre_number)
        self.air_condition = air_condition
        self.cd = cd

    def re_add_speed(self, speed):
        self.car_speed += speed
        print('经过加速后的汽车速度是' + self.car_speed)

    def re_speed_cut(self, slow_down):
        self.car_speed -= slow_down
        print('经过减速后的汽车速度是' + self.car_speed)
