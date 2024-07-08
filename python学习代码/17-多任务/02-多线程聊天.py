import socket
import sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.3', 4567))

def send_msg():
    while True:
        msg = input('请输入你想要发送的内容:')
        s.sendto(msg.encode('gbk'), ('192.168.1.3', 8989))
        if msg.lower() == 'exit':
            break

def recv_msg():
    file = open('消息记录.txt', 'a', encoding='utf8')
    while True:

        data, addr = s.recvfrom(1024)
        print('接收到来自{}地址{}端口的数据是:{}'.format(addr[0], addr[1], data.decode('gbk')),file=file)

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)
t1.start()
t2.start()
