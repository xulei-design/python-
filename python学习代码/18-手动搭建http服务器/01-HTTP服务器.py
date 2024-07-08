import socket

# HTTP都是基于tcp的socket连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.1.3', 9090))
server_socket.listen(128)

client_socket, addr = server_socket.accept()

# 从客户端的 socket 链接里获取数据
data = client_socket.recv(1024)
print('接收到来自客服端{}ip地址的{}端口发送的:{}'.format(addr[0], addr[1], data.decode('utf8')))


#在返回内容之前，需要先设置HTTP响应头
# 设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 ok\n'.encode('utf8'))
client_socket.send('content-type:text/html\n'.encode('utf8'))

# 所有的响应头设置完成以后，在换行
client_socket.send('\n'.encode('utf8'))
# 给客户端返回消息
client_socket.send('helloworld'.encode('utf8'))
