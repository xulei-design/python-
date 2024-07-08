import socket
# 1.创建一个socket对象
socket_client = socket.socket()
# 2.链接到服务端
socket_client.connect(('localhost',8888))





while True:
    # 3.发送消息
    send_msg = input("请输入要发送的消息")
    if send_msg == "exit":
        break
    socket_client.send(send_msg.encode('utf-8'))

    # 4.接受返回消息
    recv_data = socket_client.recv(1024) #1024是缓冲区大小，一般1024即可
    #recv方法是阻塞式的，既不接收到返回，就卡在这里
    print('服务端回复的消息为:',recv_data.decode("utf-8"))

# 5. 关闭链接
    socket_client.close()