import time


def cal_time(fn):
    print('我是外部函数，我被调用了！！！')
    print('fn={}'.format(fn))

    def inner(x, *args, **kwargs):
        start_time = time.time()
        s = fn(x)
        end_time = time.time()
        print('代码运行所耗的时间是{}'.format(end_time - start_time))
        return s

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


# 为什么拿不到值？怎样才能拿到值？
# print(demo())
# 因为 demo() 本质时调用 inner 函数，但是 inner 函数没有返回值，所以拿不到值
# print(demo())

# 计算一下 1~n 的和
print(demo(100000000,'good',y='world'))
