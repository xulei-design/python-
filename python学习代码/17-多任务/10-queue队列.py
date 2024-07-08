import multiprocessing
import queue

# q1 = multiprocessing.Queue() # 进程间通信
# q2 = queue.Queue() #线程间通信


# 创建队列是，可以指定最大长度。默认值是0，表示不限
q = multiprocessing.Queue(5)

q.put('hello')
q.put('god')
q.put('ok')
q.put('hi')
q.put('yes')
q.get()

print(q.full()) # 判断队列是否已满
# 往队列里放了how
# block=True:表示是阻塞，如果队列满了，就等待
# timeout 超时，等待超时以后程序会出错
# q.put('how',block=True,timeout=1) # 规定队列最多放5个，多出的会等待着无法放进去。

# q.put_nowait('how') # 等价于q.put('how',block=False)
# q.get()无法执行，q.put()是一个阻塞
# q.get()

