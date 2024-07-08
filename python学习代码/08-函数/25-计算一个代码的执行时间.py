import time # time模块可以获取当前时间

# 在代码运行之前，获取一下时间
start = time.time() #time模块里的time方法，可以获取当前时间的时间戳
# 时间戳是从 1970-01-01 00:00:00 UTC到现在的秒数
# 从 1970-01-01 00:00:00 到现在的时间是（北京时间减去8小时）
print('start=',start)   # 1614863400.7606034
x = 1
for i in range(1, 100000000):
    x += i
print(x)
# 代码运行完以后，在获取一下时间
end = time.time()
print('代码运行所耗的时间是{}'.format(end - start))