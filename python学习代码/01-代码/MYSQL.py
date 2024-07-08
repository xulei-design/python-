import pymysql
#连接mysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='XU938374',charset="utf8")
cursor = conn.cursor()

#1.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result) #(('cigarettes',), ('information_schema',), ('mysql',), ('performance_schema',), ('sakila',), ('sys',), ('world',))

#2.创建数据库
#发送指令
cursor.execute("create database db3 default charset utf8 collate utf8_general_ci")
conn.commit()

#3.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result)

#4.删除数据库
#发送指令
cursor.execute("drop database db3")
conn.commit()

#3.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result)
