import time

def cal_time(fn):
    print('我是外部函数，我被调用了！！！')
    print('fn={}'.format(fn))
    def inner():
        start_time=time.time()
        fn()
        end_time=time.time()
        print('代码运行所耗的时间是{}'.format(end_time - start_time))

    return inner

@cal_time # 第一件事是调用cal_time函数，第二件事把被装饰的函数传递给fn  语法堂
def demo():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)

# 第三件事：当再次调用demo函数时，此时的demo函数已经不再是上面的demo
print('装饰后的demo是{}'.format(demo))




