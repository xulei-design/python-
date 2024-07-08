import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.1.3', 9090))
server_socket.listen(128)

# 接收客户端请求
client_socket, client_addr = server_socket.accept()
# 接收客户端发送的内容
file_name = client_socket.recv(1024)

print('接收到来自{}客户端{}端口的消息是{}'.format(client_addr[0], client_addr[1], file_name.decode('utf8')))
