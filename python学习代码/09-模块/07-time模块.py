import datetime

v1 = datetime.datetime.now()
print(type(v1))
print(v1) #datetime类型 2023-10-15 16:35:33.384247

v2 = v1.strftime("%Y-%m-%d %H:%M:%S") #将datetime类型数据转换成字符串数据
print(type(v2))
print(v2) #2023-10-15 16:35:33

now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now_time)