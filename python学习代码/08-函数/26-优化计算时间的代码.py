import time


def cal_time(fn):
    start = time.time()

    fn()

    end = time.time()
    print('代码运行所耗的时间是{}'.format(end - start))


def demo():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)

cal_time(demo)

def foo():
    print('hello')
    time.sleep(3)
    print('world')

cal_time(foo)


