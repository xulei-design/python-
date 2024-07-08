import threading,time


def dance():
    for i in range(50):
        time.sleep(0.2)
        print('我正在跳舞')

def singe():
    for i in range(50):
        time.sleep(0.2)
        print('我正在唱歌')

# 多个任务同时执行
# python里执行多任务：多线程，多进程，多进程+多线程
# dance()
# singe()


# target 需要的是一个函数，用来指定线程需要执行的任务
t1 = threading.Thread(target=dance) # 创建了线程 1
t2 = threading.Thread(target=singe) # 创建了线程 2

# 启动线程
t1.start()
t2.start()