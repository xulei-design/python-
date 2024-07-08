# def outer(func):
#     def inner():                        #定义一个闭包函数，在闭包函数内部：
#         print("我要睡觉了")
#         func()
#         print("我要起床了")
#
#     return inner
# def sleep():
#     import random
#     import time
#     print("...睡眠中")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep)
# fn()

def outer(func):
    def inner():                        #定义一个闭包函数，在闭包函数内部：
        print("我要睡觉了")
        func()
        print("我要起床了")

    return inner
@outer
def sleep():
    import random
    import time
    print("...睡眠中")
    time.sleep(random.randint(1,5))

sleep()