import multiprocessing
import os
import time
from multiprocessing import Queue #要从进程里到Queue


def creat(x):
    for i in range(10):
        time.sleep(0.5)
        print('生产了++++++pid{}  {}'.format(os.getpid(), i))
        x.put('pid{} {}'.format(os.getpid(), i))


def consumer(x):
    for i in range(10):
        time.sleep(0.5)
        print('消费了---------{}'.format(x.get()))


if __name__ == '__main__':
    # q = Queue() # q没有定义，问题是：多进程不能共享全局变量
    q = Queue()
    # 将全局变量q传递给进程,进程间通信需要传参
    p1 = multiprocessing.Process(target=creat, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
