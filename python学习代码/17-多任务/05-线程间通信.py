# 线程之间的通信
import queue  # 线程间通信
import threading
import time


# 再输出函数中获取线程名字使用 threading.current_thread().name
def produce():
    for i in range(10):
        time.sleep(0.5)
        print('{}生产线生产了++++++面包{}号 '.format(threading.current_thread().name, i))
        q.put('生产线{}生产的面包{}号'.format(threading.current_thread().name, i))


def consumer():
    while True:
        time.sleep(1)
        # q.get()方法是一个阻塞的方法
        print('消费线{}买到了{}'.format(threading.current_thread().name,q.get()))


q = queue.Queue()  # 创建一个q对象

# 一条生产线
t1 = threading.Thread(target=produce, name='t1')
p2 = threading.Thread(target=produce, name='p2')
p3 = threading.Thread(target=produce, name='p3')
# 一条消费线
t2 = threading.Thread(target=consumer, name='t2')
t1.start()
p2.start()
p3.start()
t2.start()

# 队列结构：先进先出
# 栈结构： 先进后出
