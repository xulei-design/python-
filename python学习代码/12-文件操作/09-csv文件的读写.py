import csv # 系统内置模块
# file = open('demo.csv','w',encoding='utf8',newline='') # 打开一个文件
# w = csv.writer(file)

# w.writerow(['name','age','score','city'])
# w.writerow(['zhangsan','18','90','驻马店'])
# w.writerow(['李四','19','90','纽约'])

# w.writerows([
#     ['name','age','score','city'],
#     ['zhangsan','18','19','驻马店'],
#     ['李四','19','90','纽约']
#     ]
# )

file = open('info.csv','r',encoding='utf8',newline='')
r = csv.reader(file)
for date in r:
    print(date)



file.close()