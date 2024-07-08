import pymsql
#连接mysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='XU938374',charset="utf8")
cursor = conn.cursor()

#1.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result)