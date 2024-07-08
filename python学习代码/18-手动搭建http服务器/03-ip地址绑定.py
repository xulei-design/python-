import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.bind(('192.168.1.3', 9090)) # 在同一局域网能够访问

# 绑定(127.0.0.0)只能够通过 127.0.0.1 和 localhost 来访问 （只能本机访问）
# server_socket.bind(('127.0.0.1', 9090))
# 127.0.0.1 和 0.0.0.0 都表示本机

# 绑定（0.0.0.0）的话，能够通过局域网，本机访问
server_socket.bind(('0.0.0.0', 8090))


server_socket.listen(128)
client_socket, addr = server_socket.accept()


data = client_socket.recv(1024)
print('接收到来自客服端{}ip地址的{}端口发送的:{}'.format(addr[0], addr[1], data.decode('utf8')))



client_socket.send('HTTP/1.1 200 ok\n'.encode('utf8'))
client_socket.send('content-type:text/html\n'.encode('utf8'))


client_socket.send('\n'.encode('utf8'))
client_socket.send('helloworld'.encode('utf8'))
