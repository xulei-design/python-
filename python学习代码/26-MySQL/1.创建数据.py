import pymysql

#1.连接mysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="xu938374",charset="utf8",db='employee')
# 基于cursor发送接收数据
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#2.发送指令
cursor.execute("insert into dept(Deptno,Dname) value ('0005','销售部')")
conn.commit()

#3.关闭
cursor.close()
conn.close()