import socket

#1.创建一个socket对象
socket_server = socket.socket()
#2.绑定socker_sever的指定IP和端口
socket_server.bind(('localhost',8888))
# 3.监听端口
socket_server.listen(1)
#listen方法内接受一个整数传参数，表示接受的链接数量
#4.等待客户端链接
# result: tuple = socket_server.accept() #rusult接收到的是一个二元元组
# conn = result[0] # 客户端和服务端的链接对象
# adress = result[1] #客户端的地址信息
conn,adress = socket_server.accept()
# accept方法返回的的是二元元组(链接对象,客户端地址信息)
# 可以通过 变量1,变量2 = socket_server.accept()的形式直接接收二元元组内的两个元素
#accept()方法，是阻塞的方法，等待客户端的连接，如果没有链接，就卡在这一行不向下执行了
print(f"接收到了客户端的链接，客户端的连接地址信息是:{adress}")
# 5.接收客户端的信息,要使用客户端和服务端的本次链接对象，而非socker_server对象
data: str = conn.recv(1024).decode('utf-8')
# recv接受的参数是缓冲区大小，一般给1024即可
# recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转化为字符串对象
print(f'客服端发来的消息是:{data}')
# 6.发送回复消息
msg = input("请输入你要和客户端回复的消息:").encode('utf-8')#encode可以将字符串编码为字节数组对象
conn.send(msg)
# 7.关闭链接
conn.close()
socket_server.close()
