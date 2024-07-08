# 设计两个类：
# 一个点类，属性包括x,y坐标
# 一个Rectangle类（矩形），属性有左上角和右下角坐标
# 方法：1.计算矩形的面积，2.判断点是否在举行内部
# 实例化一个点对象，一个正方形对象，输出矩形面积，输出点是否在矩形内部
class Point(object):
    # point 方法在创建时，需要两个int类型的坐标
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def total_area(self):
        x = abs(self.bottom_right.x - self.top_left.x)
        y = abs(self.bottom_right.y - self.top_left.y)
        return x * y

    def judge(self):
        if self.bottom_right.x >= p1.x >= self.top_left.x and self.top_left.y > p1.y > self.bottom_right.y:
            print('这个点在矩形内部')
        else:
            print('这个点不在矩形内部')


p1 = Point(20, 10)
top_left = Point(4, 20)
bottom_right = Point(30, 8)

rct = Rectangle(top_left, bottom_right)
print(rct.total_area())
rct.judge()
